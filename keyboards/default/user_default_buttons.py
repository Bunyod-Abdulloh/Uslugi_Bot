from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUser


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


def uz_user_search_cbuttons(clinics: str, services: str, doctors: str, nearest_clinics: str, region: str,
                            back_main_menu: str):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"🏥 {clinics}")
            ],
            [
                KeyboardButton(text=f"💧 {services}")
            ],
            [
                KeyboardButton(text=f"💉 {doctors}")
            ],
            [
                KeyboardButton(text=f"🚶‍ {nearest_clinics}")
            ],
            [
                KeyboardButton(text=f"📍 {region}")
            ],
            [
                KeyboardButton(text=f"⬅️ {back_main_menu}")
            ]
        ],
        resize_keyboard=True
    )
    return buttons
