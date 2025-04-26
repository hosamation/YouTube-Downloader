from pytubefix import Playlist

# playlist = Playlist(input("Please enter the playlist URL: ")) # Input
playlist = Playlist("Paste URL Playlist Here")

counter = 0
# for video in playlist.videos[175:180]: # To Download specific videos from the playlist [Start : End + 1]
  
for video in playlist.videos:
  # video.streams.get_highest_resolution().download(output_path="Enter full path of the folder")
  # video.streams.get_highest_resolution().download(output_path="/home/hosamation/Downloads")   # Example
  # video.streams.get_highest_resolution().download(output_path=input("Enter full path of the folder: ")) # Input
  counter+=1
  print(f"{counter} - {video.title} Successfully Downloaded.")