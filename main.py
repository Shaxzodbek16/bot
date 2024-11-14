import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.enums import ParseMode

from config import load_config
from database.database import engine, Base
from handlers.instagram import instagram_router
from handlers.youtube import youtube_router
from utils.logger import setup_logger


async def main():
    os.makedirs("downloads", exist_ok=True)
    logger = setup_logger()
    logger.info("Starting bot")
    config = load_config()
    dp = Dispatcher()
    session = AiohttpSession(api=TelegramAPIServer.from_base('http://localhost:8081'))
    local_api = 'http://localhost:8081/bot'
    bot = Bot(token=config.tg_bot.token, base_url=local_api, session=session,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    Base.metadata.create_all(bind=engine)
    dp.include_router(youtube_router)
    dp.include_router(instagram_router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
