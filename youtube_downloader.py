from pytubefix import YouTube

video_link = YouTube(input("Please enter the video URL: "))
# video_link = YouTube("Paste URL Video Here")


video_link.streams.get_audio_only().download(output_path= input("Enter full path of the folder"))
# video_link.streams.get_highest_resolution().download(output_path= "/home/hosamation/Downloads")   # Example
print(f"{video_link.title} Successfully Downloaded.")