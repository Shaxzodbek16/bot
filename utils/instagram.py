import logging

import instaloader
import os

async def download_instagram_post(url: str) -> str | None:
    try:
        L = instaloader.Instaloader(dirname_pattern="downloads")
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target="#downloads")
        return "downloads"
    except Exception as e:
        logging.error(f"Error downloading Instagram post: {e}")
        return None