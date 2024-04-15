import editdistance

def compute_wer_editdistance(words, ref_words):
    n_SDI = editdistance.eval(words, ref_words)
    if len(ref_words) == 0:
        return 1
    return n_SDI / len(ref_words)

if __name__ == "__main__":
    # src = '今天天气很好'
    # trg = '今天天气很好啊'
    # wer = compute_wer_editdistance(src,trg)
    # wer = get_cer(src, trg)
    # print(wer)

    wrod1_path = r"C:\Users\v-zhazhai\debug\richland\F128\FreeTalk\TextScripts\3000000001-3000000500.txt"
    word2_path = r"C:\Users\v-zhazhai\debug\richland\F128\FreeTalk\output\chunk\chunk_3e2526d16d596ac4ac7aaf8641570b63_0.txt"
    word2 = []
    word1 = [x.split('\t')[-1].replace('\n','') for x in open(word2_path,'r',encoding='utf8').readlines()]
    word2 = [x.split('\t')[-1].replace('\n','') for x in open(word2_path,'r',encoding='utf8').readlines()]
    print(word1)
