from pytube import YouTube
import os

async def download_youtube_video(url: str) -> str:
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_path = os.path.join("downloads", f"{yt.title}.mp4")
        video.download(output_path="downloads")
        return download_path
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {e}")
        return None