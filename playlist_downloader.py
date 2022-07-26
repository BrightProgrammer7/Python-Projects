from pytube import YouTube
from pytube import Playlist
from pytube import streams


playlist_link = input('Enter playlist link : ')

playlist = Playlist(playlist_link)

for video in playlist:
    link = YouTube(video)
    link.streams.get_highest_resolution().download(
        "C:/Users/abdel/Videos/Youtube/Playlist")

def finish():
    print("Download Done")

playlist.register_on_complete_callback(finish())