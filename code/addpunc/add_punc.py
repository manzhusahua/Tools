import json
import onnxruntime
import torch
import numpy as np
import shutil

from torch.nn.utils.rnn import pad_sequence
from typing import Dict, Tuple, List, Sequence, Iterable
from torch import Tensor

from BPEmb import BPEmain

import os

def tag2str(lex: list, tag: list) -> str:
    temp = []
    if len(lex) != len(tag):
        print(lex)
        print(tag)
        return None

    for i, j in zip(lex, tag):
        if j == 2:
            temp.append(i+"，")
        elif j == 3:
            temp.append(i+"。")
        elif j == 4:
            temp.append(i+"？")
        else:
            temp.append(i)
    
    return " ".join(temp)

## Vocabulary that stores the word<->index mapping and word counts.
#
#  Receives a WID file and converts it to a vocab object for use in data processing and the model.
class Vocab(object):
    ##  The constructor
    #   @param self The object pointer
    #   @param wid_file The wid/vocabulary file in "wordTABindexTABcount" format to construct the Vocab from
    def __init__(self, wid_file):
        ## The word to index mapping.
        self.word2idx = {}
        ## The index to word mapping
        self.idx2word = None
        ## The padding id
        self.pad_id = 0
        ## The first id in the vocab
        self.first = self.pad_id
        ## Beginning of text token
        self.bot = '<bot>'
        ## End of sentence token
        self.eos = '<s>'
        ## Token for unknown words
        self.unk = '<unk>'
        ## Padding token
        self.pad = '<pad>'
        ## Required vocab tokens
        # self.required = [self.eos, self.unk]
        self.required = []
        ## Restricted vocab tokens
        # self.restricted = [self.pad, self.bot]
        self.restricted = []
        ## Vocab tokens with zero weight in loss calculations
        self.zero_weight = {self.pad, self.bot}
        ## The unigram probabilities
        self.wfreq = None
        wfreq_tmp = {}

        assert (os.path.exists(wid_file))

        with open(wid_file, 'r', encoding='utf-8') as f_in:
            lines = [line.strip('\r\n') for line in f_in]

        # assume that wid are contiguous
        for wid, line in enumerate(lines):
            w, c = line.split('\t')
            wid = int(wid) + self.first
            c = float(c)
            if w in self.word2idx:
                print("[data.vocab] ignoring duplicate entry: {w}")
            elif c < 0:
                raise IOError(f"[data.vocab] {w} has a negative count of {c}")
            else:
                self.word2idx[w] = wid
                wfreq_tmp[w] = c

        # Ensure non-empty vocab
        assert (len(wfreq_tmp) > 0)

        invalid = False
        for r in self.required:
            if r not in self.word2idx:
                print(f"[data.vocab] Error: required_word={r} not in wid_file={wid_file}")
                invalid = True
        if invalid:
            raise ValueError(f"[data.vocab] missing required words in wid_file={wid_file}")

        invalid = False
        for r in self.restricted:
            if r in self.word2idx:
                print(f"[data.vocab] Error: restricted_word={r} in wid_file={wid_file}")
                invalid = True
        if invalid:
            raise ValueError(f"[data.vocab] restricted words in wid_file={wid_file}")

        # # Add pad  to vocab with smallest possible sampling frequency of 1
        # self.word2idx[self.pad] = self.pad_id
        # wfreq_tmp[self.pad] = 0.  # don't want it to appear as a noise sample

        # # Add bot to vocab with smallest possible sampling frequency of 1
        # self.word2idx[self.bot] = len(self.word2idx)
        # wfreq_tmp[self.bot] = 0.  # don't want it to appear as a noise sample

        # Ensure vocab size is multiple of 8 for FP16 support
        null_count = 0
        while len(self.word2idx) % 8 != 0:
            null_word = "fp16_null_%d" % null_count
            self.word2idx[null_word] = len(self.word2idx)
            wfreq_tmp[null_word] = 0.  # don't want it to appear as a noise sample
            null_count += 1
            self.zero_weight.add(null_word)
        ## The index to word map
        self.idx2word = [''] * len(self.word2idx)
        ## The weights for each word. For use with the loss function
        self.weights = [1] * len(self.word2idx)
        # Get word counts
        wfreq = np.zeros(len(self.word2idx), dtype=np.double)
        for w, i in self.word2idx.items():
            # print("{}: {}".format(i, w))
            try:
                self.idx2word[i] = w
                wfreq[i] = wfreq_tmp[w]
                if w in self.zero_weight:
                    self.weights[i] = 0
            except:
                pass
        # convert to unigram probs
        wfreq /= wfreq.sum()
        ## The word frequencies / unigram probs
        self.wfreq = wfreq
        ## The beginning of text id
        self.bot_id = self.word2idx[self.bot]
        ## The end of sentence id
        self.eos_id = self.word2idx[self.eos]
        ## The id for unknown words
        self.unk_id = self.word2idx[self.unk]

    ##  Encode a list of strings using the vocabulary
    #   @param self The object pointer
    #   @param words The list of strings to encode
    #   @param vocab_size The maximum vocab size to use (overrides internal vocab size)
    #   @return A list of vocabulary indices
    def encode(self, words: List[str], vocab_size: int = None) -> List[int]:
        if vocab_size:
            return [self.word2idx[w] if w in self.word2idx and self.word2idx[w] < vocab_size else self.unk_id for w in
                    words]
        else:
            return [self.word2idx[w] if w in self.word2idx else self.unk_id for w in words]

    ##  Decode a list of indicies using the vocabulary
    #   @param self The object pointer
    #   @param indices The list of vocabulary indices to decode
    #   @return The word that correspond to the indices as a space separated string
    def decode(self, indices: List[int]) -> str:
        return " ".join(self.idx2word[idx] for idx in indices)

    ##  Mask words in the vocab
    #   Sets the weights to the words to zero
    #   @param self The object pointer
    #   @param words The list of words to mask
    def mask_words(self, words: List[str]):
        for word in words:
            if word not in self.word2idx:
                raise ValueError(f"[data.vocab.mask_words] {word} is not in vocab")
            if word in self.required:
                raise ValueError(f"[data.vocab.mask_words] cannot mask {word} as it is required")
            wid = self.word2idx[word]
            self.zero_weight.add(word)
            self.weights[wid] = 0

    ##  The number of words in the vocab
    #   @param self The object pointer
    #   @return The vocabulary size
    def __len__(self) -> int:
        return len(self.idx2word)



def tokenize_iterable(input_data: Iterable[str], vocabs, bpe: None,
                      keep_feats: Sequence[int] = None, rank: int = 0, world_size: int = 1,
                      vocab_sizes: Sequence[int] = None, bos_token: str = None, eos_token: str = None,
                      permit_empty: bool = False, remove_last: bool = False) -> Tuple[
    List[Tuple[List[Tensor], int]], int]:
    data = []
    line_num = -1
    for line_num, line in enumerate(input_data):
        if world_size > 1 and line_num % world_size != rank:
            continue
        features = line.strip('\r\n').split("\t")
        if not features[0] and not permit_empty:
            raise ValueError("[prep_utils.tokenize_iterable] Empty lines must be handled prior to tokenization")
        # Keep all features unless specified
        if keep_feats is None:
            keep_feats = range(len(features))
            # Ensure alignment between vocab files and features
            if len(keep_feats) != len(vocabs):
                raise ValueError(
                    f"[prep_utils.tokenize_iterable] The number of features ({len(features)}) must match the number of "
                    f"vocabs ({len(vocabs)}), mismatch on {line_num}")
        # Create list of features. Each feature is a tuple of words.
        seqs = []
        seq_len = 0
        for pos, feat in enumerate(keep_feats):
            if bpe:
                if remove_last:
                    tokens = bpe[pos].apply_bpe(features[feat].rsplit(maxsplit=1)[0])
                else:
                    tokens = bpe[pos].apply_bpe(features[feat])
            else:
                if remove_last:
                    tokens = features[feat].split()[:-1]
                else:
                    tokens = features[feat].split()
            if bos_token and eos_token:
                tokens = [bos_token] + tokens + [eos_token]
            elif bos_token:
                tokens = [bos_token] + tokens
            elif eos_token:
                tokens = tokens + [eos_token]

            seq = torch.as_tensor(
                vocabs[feat].encode(tokens, vocab_size=vocab_sizes[feat] if vocab_sizes else None),
                dtype=torch.long)
            # Ensure same sequence length for each feature
            if seq_len == 0:
                seq_len = seq.numel()
            elif seq.numel() != seq_len:
                raise ValueError(
                    "[prep_utils.tokenize_iterable] The same number of tokens must be provided for all features, "
                    "mismatch on {}".format(line_num))
            seqs.append(seq)
        data.append((seqs, seq_len))
    return data, line_num + 1

def batch_features(batch: List[Tuple[List[Tensor], int]]) -> Tuple[Tuple[Tensor, ...], Tensor]:
    seq_lens = torch.as_tensor([seq[1] for seq in batch])
    feats = tuple(pad_sequence(feat) for feat in zip(*(sample[0] for sample in batch)))
    return feats, seq_lens

def parse_float_iterable(input_data: Iterable[str], rank: int = 0, world_size: int = 1,
                         num_dense_tok: int = None, dense_tok2seq: int = None) -> Tuple[
    List[Tuple[Tensor, ...]], List[Tuple[Tensor, ...]], int]:
    tok_level = []
    seq_level = []
    line_num = -1
    for line_num, line in enumerate(input_data):
        if world_size > 1 and line_num % world_size != rank:
            continue
        feats = parse_float(line, as_tensor=True)
        num_feats = len(feats)
        if dense_tok2seq:
            if dense_tok2seq > num_feats:
                raise IOError(
                    f"Requested to convert {dense_tok2seq} tok-level float feats to seq-level, but only found {num_feats}")
            seq_level.append(feats[-dense_tok2seq:])
            num_feats -= dense_tok2seq
        if num_dense_tok:
            if num_dense_tok > num_feats:
                raise IOError(
                    f"Requested to convert {num_dense_tok} tok-level float feats, but only found {num_feats}")
            tok_level.append(feats[:num_dense_tok])
        elif num_feats > 0:
            tok_level.append(feats[:num_feats])
    return tok_level, seq_level, line_num + 1

def combine_features(feat_list: Iterable[Tensor], seq_len: int, batch_size: int) -> Tensor:
    reshaped = []
    for feat in feat_list:
        if feat.size(0) % seq_len != 0:
            raise ValueError(
                "[prep_utils.combine_features] Different number of float feats for each timestep")
        emb_size = feat.size(0) // seq_len
        # Move embs to last dim
        if emb_size > 1:
            feat = feat.view(seq_len, -1, batch_size)
            feat = feat.transpose(1, 2)
        else:
            feat = feat.view(seq_len, batch_size, 1)
        reshaped.append(feat)
    if len(reshaped) > 1:
        return torch.cat(reshaped, dim=2)
    else:
        return reshaped[0].contiguous()

def parse_float(line: str, as_tensor: bool = False):
    if as_tensor:
        return tuple(torch.as_tensor(list(map(float, seq.split()))) for seq in line.strip('\r\n').split("\t"))
    return tuple(np.asarray(seq.split(), dtype=np.float) for seq in line.strip('\r\n').split("\t"))

def prep_batch(batch: List[str], vocab, bpes, enc_vocab_sizes, dense_tok_batch: List[str] = None):
    # Tuple[List[Tuple[List[Tensor], int]], int]
    data, batch_size = tokenize_iterable(batch, vocab, bpe=bpes,
                                                    vocab_sizes=enc_vocab_sizes, permit_empty=True)
    # Tuple[Tuple[Tensor, ...], Tensor]
    feats, seq_lens = batch_features(data)
    if dense_tok_batch:
        seq_len = seq_lens.max().item()
        tok_level, _, num_dense = parse_float_iterable(dense_tok_batch)
        if num_dense != batch_size:
            raise IOError("Incorrect number of token-level dense features")
        tok_level = combine_features((pad_sequence(feat) for feat in zip(*tok_level)), seq_len,
                                                batch_size)
    else:
        tok_level = None
    return {"tok_seqs": feats, "length_scalars": seq_lens, "tok_level": tok_level}

def seqs_to_tag(src, lengths, blank_ids, tgt=None, shift: int = 0, bot_ids=None, tgt_feats: int = None):
    # Length of padding for shift/bot
    if bot_ids is None:
        extra_toks = shift
    else:
        # Extra pad for bot token
        extra_toks = shift + 1
    srcs = []
    tgts = []
    # First stype is source
    if extra_toks > 0:
        for feat_idx, feat_data in enumerate(src):
            t, b = feat_data.size()
            t += extra_toks
            seq = feat_data.new_zeros((t, b))
            # Add bot
            if bot_ids is not None:
                seq[0, :] = bot_ids[feat_idx]
                offset = 1
            else:
                offset = 0
            # Copy original sequence
            seq[offset:t - shift, :] = feat_data
            # Add blank ids
            for i in range(offset, shift + offset):
                seq.scatter_(0, lengths.view(1, -1) + i, blank_ids[feat_idx])
            srcs.append(seq)
    else:
        srcs = src
    if tgt is None:
        # Same size as src
        seq = srcs[0].new_zeros(srcs[0].size()).view(-1)
        # Set non-zero inputs to valid, then readd padding
        # as_tuple=False is 20% faster than as_tuple=True and uses much less memory
        seq[srcs[0].view(-1).nonzero(as_tuple=False)] = 1
        seq = seq.view(srcs[0].size())
        seq[:extra_toks] = 0
        # Repeat mask for each feat
        tgts = [seq] * tgt_feats
    elif extra_toks > 0:
        for feat_idx, feat_data in enumerate(tgt):
            t, b = feat_data.size()
            t += extra_toks
            seq = feat_data.new_zeros((t, b))
            # Copy original sequence, add padding to front
            seq[extra_toks:, :] = feat_data
            tgts.append(seq)
    else:
        tgts = tgt
    shifted_lengths = lengths.add(extra_toks)
    return srcs, tgts, shifted_lengths

def get_predictions_from_ONNX(onnx_session, vocab, pre_batch, lang_shift):
    """Perform predictions with ONNX runtime
    
    :param onnx_session: onnx model session
    :type onnx_session: class InferenceSession
    :param img_data: pre-processed numpy image
    :type img_data: ndarray with shape 1xCxHxW
    :return: scores with shapes
            (1, No. of classes in training dataset) 
    :rtype: numpy array
    """
    bpes = None
    enc_vocab_sizes = [len(vocab[0].word2idx)]
    batch = prep_batch(pre_batch, vocab, bpes, enc_vocab_sizes, dense_tok_batch=None)
    # Move batch to GPU

    src = batch["tok_seqs"]
    lengths = batch["length_scalars"]
    # self.blank_ids = [vocab.word2idx["<blank>"] for vocab in self.vocab]
    blank_ids = [vocab[0].word2idx["<blank>"]]
    bot_ids = None
    num_tgt_feats = 1
    src, tgt_mask, shifted_lengths = seqs_to_tag(src, lengths, blank_ids, shift=0,
                                                                bot_ids=bot_ids, tgt_feats=num_tgt_feats)

    src = src[0].T
    tgt = tgt_mask[0].T
    src = torch.cat([src, torch.tensor([blank_ids]*lang_shift)])
    tgt = torch.cat([torch.tensor([[0]]*lang_shift), tgt])

    input_name_1 = onnx_session.get_inputs()[0].name
    input_name_2 = onnx_session.get_inputs()[1].name
    label_name = onnx_session.get_outputs()[0].name
    pred_onx = onnx_session.run([label_name], {input_name_1: np.atleast_2d(np.array(src)).astype('int64'), input_name_2: np.atleast_2d(np.array(tgt)).astype('int64')})

    return pred_onx

def add_punc(input_transcription_file, temp_output_folder, output_transcription_withpunc_file):
    # input_transcription_file = clean_word2(input_transcription_file)
    try:
        bpe_in_file = input_transcription_file
        if not os.path.exists(bpe_in_file):
            return None

        if not os.path.exists(temp_output_folder):
            os.makedirs(temp_output_folder, exist_ok=True)
        bpe_out_file = os.path.join(temp_output_folder, "bpe.out.text")
        BPEmain(bpe_in_file, bpe_out_file)
        if not os.path.exists(bpe_out_file):
            return None

        onnx_model_path = "/mnt/c/Users/v-zhazhai/debug/aml_tools/richland/zh-cn/punc/zhCN/punc.onnx"
        try:
            session = onnxruntime.InferenceSession(onnx_model_path)
            print("ONNX model loaded...")
        except Exception as e: 
            print("Error loading ONNX file: ", str(e))
            return None
        
        lang_shift = 8
        batch_size = 1
        vocab = [Vocab("zhCN/w2i.txt")]
        

        # Text sample
        # batch = [['今天','天气', '炎热', '吗'], ['0月00日', '我', '跟', '老公', '过', '纪念日'], ['火车', '站', '在', '哪里', '呢'], ['猫', '喵', '喵', '叫']]

        lines = open(bpe_out_file, "r").readlines()
        lines = [line.strip() for line in lines]
        lines = " ".join(lines).split()
        scores = get_predictions_from_ONNX(session, vocab, lines, lang_shift)
        result = tag2str(lines, scores[0].tolist())
        if result is not None:
            output_file_path = os.path.join(temp_output_folder, output_transcription_withpunc_file)
            with open(output_file_path, "w", encoding="utf-8") as f:
                # f.write(result)
                f.write(clean_word1(result))
        
    except Exception as e:
        print("Error: ", str(e))


def clean_word1(withpuncword):
    word = ""
    n=0
    while n<len(withpuncword.split(' ')):
        if withpuncword.split(' ')[n][-1].lower() in 'qwertyuiopasdfghjklmnbvcxz' and withpuncword.split(' ')[n][0].lower() in 'qwertyuiopasdfghjklmnbvcxz':
            word = word+withpuncword.split(' ')[n]+' '
        elif withpuncword.split(' ')[n][-1].lower() in 'qwertyuiopasdfghjklmnbvcxz' and withpuncword.split(' ')[n][0].lower() not in 'qwertyuiopasdfghjklmnbvcxz':
            word = word+withpuncword.split(' ')[n]+' '
        else:
            word = word+withpuncword.split(' ')[n]
        n+=1
    return word

def clean_word2(richland_files):
    with open(richland_files, "r",encoding='utf8') as file:
        data = json.load(file)
    word  = data["Results"][0]["FullTranscription"]
    # print(word) 
    # word = open(richland_files,'r',encoding='utf8').readlines()[0].replace('\n','')
    
    with open(richland_files.replace(".json","_clean.txt"),'w',encoding='utf8') as s:
        # chinese_str = word.encode('utf-8').decode('unicode_escape')
        # s.writelines(chinese_str+'\n')
        s.writelines(word+'\n')
    
    return richland_files.replace(".json","_clean.txt")

if __name__ == "__main__":
    import glob
    # add_punc("bpe.in.text", "temp", "output_withpunc.txt")
    richland_dir = "/mnt/c/Users/v-zhazhai/Downloads/test/2"
    temp_dir = "/mnt/c/Users/v-zhazhai/Downloads/test/2"
    
    
    for richland_json in glob.glob(os.path.join(richland_dir, "**", "*.txt"), recursive=True):
        add_punc_files = richland_json.split("/")[-1].replace(".txt", "_withpunc.txt")
        add_punc(richland_json, temp_dir, add_punc_files)
    