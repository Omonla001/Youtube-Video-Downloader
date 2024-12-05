#!/usr/bin/env python3
import os
import sys
import subprocess
import yt_dlp

def download_video(video_url):
    try:
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Save video with its title as the filename
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading '{video_url}'...")
            ydl.download([video_url])
            print(f"Downloaded '{video_url}' successfully.")
    except yt_dlp.utils.DownloadError as e:
        print(f"A network error occurred: {e}")
        user_input = input("Network error occurred. Do you want to retry? (yes/no): ").strip().lower()
        if user_input == 'yes':
            download_video(video_url)
        else:
            print("Skipping this video.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tubeVideo.py <video_url1> <video_url2> ...")
        sys.exit(1)

    video_urls = sys.argv[1:]

    for url in video_urls:
        try:
            download_video(url)
        except Exception as e:
            print(f"An unexpected error occurred while processing '{url}': {e}")
            continue

if __name__ == "__main__":
    main()
