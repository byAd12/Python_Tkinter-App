import sys, os
import yt_dlp as youtube_dl
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from pytube import YouTube
#############################################################################################
def mp4_mp3(ruta):
    try:
        video = VideoFileClip(ruta)
        video.audio.write_audiofile(r"C:\Users\{}\Music\convertido.mp3".format(os.getlogin()), codec="mp3")
    except Exception as e:
        print("ERROR: ", e)

def ph_yt_mp4(url):
    try:
        with youtube_dl.YoutubeDL({"format": "best", "outtmpl": "C:/Users/{}/Videos/%(title)s.%(ext)s".format(os.getlogin()), "nooverwrites": True, "no_warnings": False, "ignoreerrors": True}) as ydl:
            ydl.download([url])
    except Exception as e:
        print("ERROR: ", e)
#############################################################################################
if str(sys.argv[1]) == "func1":
    mp4_mp3(str(sys.argv[2]))
if str(sys.argv[1]) == "func2":
    ph_yt_mp4(str(sys.argv[2]))