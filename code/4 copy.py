import re

def wrap_with_voice_and_lang_tags(input_text, voice_name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)'):
    #input_text = html.escape(input_text)
    print("Raw_input_text: %s" % input_text)
    # Step 1: Wrap phonemes
    phoneme_pattern = r"/([^/]+)/"
    input_text = re.sub(phoneme_pattern, lambda m: f"<phoneme alphabet='ipa' ph='{m.group(1)}'>/{m.group(1)}/</phoneme>", input_text)

    print(("Added phoneme tag: %s" % input_text))
    # Step 2: Wrap English words/symbols and phoneme tags
    lang_pattern = r"((?:<phoneme[^>]+>[^<]+</phoneme>|[A-Za-z0-9\-'/]+)(?:\s+(?:<phoneme[^>]+>[^<]+</phoneme>|[A-Za-z0-9\-'/]+))*)([.,!?]?)"
    
    def wrap_lang(m):
        full = m.group(0)
        return f"<lang xml:lang='en-US'>{full}</lang>"

    input_text = re.sub(lang_pattern, wrap_lang, input_text)

    print("Added lang tag: %s" % input_text)

    # Step 3: Merge contiguous lang tags
    input_text = input_text.replace("</lang>.  <lang xml:lang='en-US'>", ". ")
    input_text = input_text.replace("</lang>. <lang xml:lang='en-US'>", ". ")
    input_text = input_text.replace("</lang>.<lang xml:lang='en-US'>", ". ")
    input_text = input_text.replace("</lang> . <lang xml:lang='en-US'>", ". ")
    input_text = input_text.replace("</lang>,  <lang xml:lang='en-US'>", ", ")
    input_text = input_text.replace("</lang>, <lang xml:lang='en-US'>", ", ")
    input_text = input_text.replace("</lang> , <lang xml:lang='en-US'>", ", ")
    input_text = input_text.replace("</lang>,<lang xml:lang='en-US'>", ", ")
    input_text = input_text.replace("</lang>  <lang xml:lang='en-US'>", " ")
    input_text = input_text.replace("</lang> <lang xml:lang='en-US'>", " ")
    input_text = input_text.replace("</lang><lang xml:lang='en-US'>", "")
    input_text = input_text.replace("</lang> \"<lang xml:lang='en-US'>", " \"")
    input_text = input_text.replace("</lang>\", <lang xml:lang='en-US'>", "\",")
    input_text = input_text.replace("</lang> .", " .</lang>")
    input_text = input_text.replace("</lang>.", ".</lang>")
    input_text = input_text.replace("</lang>\".", "\".</lang>")
    #input_text = input_text.replace("</lang>。", "。</lang>")
    #input_text = input_text.replace("</lang> 。", " 。</lang>")
    #input_text = input_text.replace("</lang>\"。", "\"。</lang>")
    print("Merged lang tag: %s" % input_text)
    # Step 4: Wrap with voice tag
    return f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='en-US'><voice name='{voice_name}'>{input_text}</voice></speak>"

if __name__=="__main__":
    input_text = "/iːd/ 德国东部 "
    wrap_with_voice_and_lang_tags(input_text, voice_name='Microsoft Server Speech Text to Speech Voice (zh-CN, YunyangNeural)')
