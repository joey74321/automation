# youtube_downloader.py

from pytube import YouTube


def download_video(url, output_path="."):
    try:
        # Get YouTube video
        yt = YouTube(url)

        # Get highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download video
        video_stream.download(output_path)

        return f"Video downloaded successfully. Saved at: {output_path}/{yt.title}.mp4"
    except Exception as e:
        return f"Error: {str(e)}"
