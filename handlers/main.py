from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.inline import get_website_keyboard
from handlers.youtube import youtube_router
from handlers.instagram import instagram_router

main_router = Router()

@main_router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Welcome to our bot! Please select an option from the menu.", reply_markup=get_website_keyboard())

@main_router.callback_query()
async def handle_callback(callback: CallbackQuery):
    if callback.data == "youtube_downloader":
        await callback.message.answer("You selected the YouTube downloader.")
        await youtube_router.handle(callback.message)
    elif callback.data == "instagram_downloader":
        await callback.message.answer("You selected the Instagram downloader.")
        await instagram_router.handle(callback.message)
    await callback.answer()
