from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_main_default_button(communicate_doctor: str, search: str, profile: str):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"📱 {communicate_doctor}")
            ],
            [
                KeyboardButton(text=f"🔍 {search}")
            ],
            [
                KeyboardButton(text=f"👤 {profile}")
            ]
        ],
        resize_keyboard=True
    )
    return buttons
