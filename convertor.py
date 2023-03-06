from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

folder = 'C:/Users/aleks/Downloads/m'

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)