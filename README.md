# YouTube Downloader Toolkit

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple and efficient command-line toolkit for downloading YouTube content, including videos, playlists, audio, and subtitles.

## Description

This Python script provides a user-friendly, menu-driven interface to download various types of content from YouTube. It leverages the `pytubefix` library to interact with YouTube and handle the downloads. The script is designed to be straightforward, prompting the user for all necessary information, such as URLs and save locations.

## Features

- **Menu-Driven Interface**: Easy-to-use command-line menu to select download options.
- **Single Video Download**: Download a single YouTube video in the highest available resolution.
- **Playlist Download**: Download all videos from a YouTube playlist in one go.
- **Audio Extraction**: Download only the audio from a single video or an entire playlist.
- **Subtitle Download**: Fetch and save English subtitles for any video as a `.txt` file.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1.  Clone the repository to your local machine:

    ```bash
    git clone https://github.com/hosamation/YouTube-Downloader.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd YouTube-Downloader
    ```

3.  Install the required dependency:
    ```bash
    pip install pytubefix
    ```

## How to Use

1.  Run the script from your terminal:

    ```bash
    python3 youtube_downloader.py
    ```

2.  You will be presented with a menu of options:

    ```
    YouTube Downloader
    ==================
    1. Download a single YouTube video
    2. Download a YouTube playlist
    3. Download audio from a YouTube video
    4. Download audio from a YouTube playlist
    5. Download video subtitles
    ==================
    ```

3.  Enter the number corresponding to your desired action (e.g., `1` to download a single video).

4.  The script will then prompt you to enter the YouTube URL and the full path to the folder where you want to save the content.

5.  The download will begin, and the script will print progress and completion messages to the console.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
