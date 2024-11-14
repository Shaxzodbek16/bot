from aiogram import Router, F
from aiogram.types import Message
from utils.youtube import download_youtube_video
import os

youtube_router = Router()


@youtube_router.message(F.text.startswith('y '))
async def youtube_download_handler(message: Message):
    try:
        url = message.text[2:].strip()
        await message.answer("⏳ Processing your YouTube video...")

        file_path = await download_youtube_video(url)
        if file_path and os.path.exists(file_path):
            await message.answer_video(
                video=open(file_path, 'rb'),
                caption="✅ Here's your video!"
            )
            os.remove(file_path)  # Clean up after sending
        else:
            await message.answer("❌ Sorry, couldn't download this video.")
    except Exception as e:
        await message.answer("❌ An error occurred while processing your request.")
        logging.error(f"YouTube download error: {e}")
