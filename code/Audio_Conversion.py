import moviepy.editor as moviepy
import os

def webm_to_wav(inputdir,output):
    for line in os.listdir(inputdir):
        clip = moviepy.VideoFileClip(os.path.join(inputdir,line))
        clip.audio.write_audiofile(os.path.join(output,line.replace(".webm",".wav")))


if __name__ == "__main__":
    inputdir = r"C:\Users\v-zhazhai\Downloads\EMNS\raw_webm"
    outputdir = r"C:\Users\v-zhazhai\Downloads\EMNS\raw_webm_wave"
    if not os.path.exists(outputdir):
        os.makedirs(outputdir, exist_ok=True)
    webm_to_wav(inputdir,outputdir)