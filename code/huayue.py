import os,shutil

style_map = {"GeneralChat":"10000","Story":"10100","Explanation":"10200","Speech":"10300","Recipe":"10400","TrueConfessions":"10500","Poem":"10600","Interjection":"10700","Advertisement":"10800","DialogueOfGamingCharacter":"10900","documentary narration":"11000","E-learning":"11100","Meditation":"11200","MovieNarration":"11300","TalkShow":"11400","News":"11500","Podcast":"11600","SocialMedia":"11700","Audiobook":"11800"}

def speech_foder(inputdir,outputdir):

    Alignment_input = os.path.join(inputdir,"Alignment","ForcedAlignment.Phone.WithSR")
    for home,dirs,files in os.walk(Alignment_input):
        for filename in files:
            if filename[:5] in style_map.values():
                style = list(style_map.keys())[list(style_map.values()).index(str(filename[:5]))]
                m = int(filename[6:].split('.')[0])//500
                countname = "{}-{}".format(str(filename[:5])+str(500*(m)).zfill(7),str(filename[:5])+str((m+1)*500).zfill(7))
                # print(countname)
                Alignment_output = os.path.join(outputdir,"Alignment","ForcedAlignment.Phone.WithSR",style,countname)
                if not os.path.exists(Alignment_output):
                    os.makedirs(Alignment_output, exist_ok=True)
                shutil.copyfile(os.path.join(home,filename),os.path.join(Alignment_output,filename))

                # countname = "{}-{}".format(str(filename[:5])+str(0).zfill(7),str(filename[:5])+str(m).zfill(7))
                # print(countname)

def alignment_floder(inputdir):
    print()

def split_floder(inputdir,outputdir):
    # Alignment split
    speech_foder(inputdir,outputdir)

    #Speech split
    Speech_path = os.path.join(inputdir,"Speech")


if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Desktop\Jourdan"
    outputdir = r"C:\Users\v-zhazhai\Desktop\Jourdan_out"
    speech_foder(inputdir,outputdir)