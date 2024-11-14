from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_website_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="Visit Our Website",
        url="https://shaxzodbek.com/"
    ))
    return keyboard
