from pytube import Playlist

# playlist = Playlist(input("Please enter the playlist URL: "))
playlist = Playlist("Paste URL Playlist Here")

# for video in playlist.videos[0:2]: # To Download specific videos from the playlist [Start : End + 1]
for video in playlist.videos:
  video.streams.get_highest_resolution().download(output_path="Enter full path of the folder")
  # video.streams.get_highest_resolution().download(output_path="/home/hosamation/Downloads")   # Example
  video.register_on_complete_callback(finish())