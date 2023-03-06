from pytube import YouTube
from pytube import Playlist

string = "https://www.youtube.com/watch?v=gFtjckFWRZM&list=PLxKNuQo2VDWdqYcadd3NkLCcebUQIymgV"

playlist = Playlist(string)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download()

