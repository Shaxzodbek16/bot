from aiogram import Router, F
from aiogram.types import Message
from utils.instagram import download_instagram_post
import os
import glob

instagram_router = Router()


@instagram_router.message(F.text.startswith('i '))
async def instagram_download_handler(message: Message):
    try:
        url = message.text[2:].strip()
        await message.answer("⏳ Processing your Instagram post...")

        download_dir = await download_instagram_post(url)
        if download_dir:
            # Send all downloaded files (could be multiple for carousel posts)
            media_files = glob.glob(f"{download_dir}/*.[jJ][pP][gG]")
            for file_path in media_files:
                await message.answer_photo(
                    photo=open(file_path, 'rb'),
                    caption="✅ Here's your post!"
                )
                os.remove(file_path)  # Clean up after sending
            os.rmdir(download_dir)  # Remove empty directory
        else:
            await message.answer("❌ Sorry, couldn't download this post.")
    except Exception as e:
        await message.answer("❌ An error occurred while processing your request.")
        logging.error(f"Instagram download error: {e}")

# main.py