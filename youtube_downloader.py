from pytubefix import YouTube, Playlist

def main():
    print("YouTube Downloader")
    print("==================")
    print("1. Download a single YouTube video")
    print("2. Download a YouTube playlist")
    print("3. Download audio from a YouTube video")
    print("4. Download audio from a YouTube playlist")
    print("5. Download video subtitles")
    print("==================")

    choice = input("Please enter your choice (1-5): ")

    if choice == '1':
        download_video()
    elif choice == '2':
        download_playlist()
    elif choice == '3':
        download_audio()
    elif choice == '4':
        download_playlist_audio()
    elif choice == '5':
        download_subtitle()
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

def download_video():
    """Downloads a single YouTube video in the highest available resolution."""
    try:
        video_link = YouTube(input("Please enter the video URL: "))
        output_path = input("Enter the full path of the folder to save the video: ")
        print(f"Downloading '{video_link.title}'...")
        video_link.streams.get_highest_resolution().download(output_path=output_path)
        print(f"'{video_link.title}' successfully downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_playlist():
    """Downloads all videos from a YouTube playlist in the highest resolution."""
    try:
        playlist_link = Playlist(input("Please enter the playlist URL: "))
        output_path = input("Enter the full path of the folder to save the playlist: ")
        print(f"Downloading playlist '{playlist_link.title}'...")
        for video in playlist_link.videos:
            print(f"  - Downloading '{video.title}'...")
            video.streams.get_highest_resolution().download(output_path=output_path)
        print(f"Playlist '{playlist_link.title}' successfully downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio():
    """Extracts and downloads only the audio from a single YouTube video."""
    try:
        video_link = YouTube(input("Please enter the video URL: "))
        output_path = input("Enter the full path of the folder to save the audio: ")
        print(f"Downloading audio for '{video_link.title}'...")
        video_link.streams.get_audio_only().download(output_path=output_path)
        print(f"Audio for '{video_link.title}' successfully downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_playlist_audio():
    """Extracts and downloads the audio from all videos in a YouTube playlist."""
    try:
        playlist_link = Playlist(input("Please enter the playlist URL: "))
        output_path = input("Enter the full path of the folder to save the audio files: ")
        print(f"Downloading audio for playlist '{playlist_link.title}'...")
        for video in playlist_link.videos:
            print(f"  - Downloading audio for '{video.title}'...")
            video.streams.get_audio_only().download(output_path=output_path)
        print(f"Audio for playlist '{playlist_link.title}' successfully downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_subtitle():
    """Downloads the English subtitles for a video and saves them as a .txt file."""
    try:
        video_link = YouTube(input("Please enter the video URL: "))
        output_path = input("Enter the full path of the folder to save the subtitle: ").strip()
        print(f"Downloading subtitles for '{video_link.title}'...")
        # Attempt to get 'a.en' (auto-generated English) or fallback to 'en'
        caption = video_link.captions.get('a.en') or video_link.captions.get('en')
        if caption:
            file_path = f"{output_path}/{video_link.title}.txt"
            caption.save_captions(file_path)
            print(f"Subtitles for '{video_link.title}' successfully downloaded to {file_path}.")
        else:
            print("No English subtitles found for this video.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
