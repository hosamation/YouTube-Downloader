from pytube import YouTube

# video_link = YouTube(input("Please enter the video URL: "))
video_link = YouTube("Paste URL Video Here")

def finish():
  print("Download Done!")

video_link.streams.get_highest_resolution().download(output_path= input("Enter full path of the folder"))
# video_link.streams.get_highest_resolution().download(output_path= "/home/hosamation/Downloads")   # Example
video_link.register_on_complete_callback(finish())