import yt_dlp

def download_youtube_video(video_url, output_path='downloads/'):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_path (str): The directory where the video will be saved.
                           Defaults to 'downloads/'.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best available video and audio, or best overall
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Output template with title and extension
        'merge_output_format': 'mp4',  # Merge into MP4 format
        'noplaylist': True,  # Don't download entire playlist if URL is for a playlist item
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    # Example usage:
    video_link = "https://www.youtube.com/watch?v=HMKVe29uP58"
    download_directory = input("Enter the download directory (press Enter for default 'downloads/'): ") or 'downloads3/'

    download_youtube_video(video_link, download_directory)
