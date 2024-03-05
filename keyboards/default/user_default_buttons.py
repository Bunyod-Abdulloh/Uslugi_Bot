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


#  Klinika bo'yicha qidirish, Shifokor sohasi bo'yicha qidirish Manzil bo'yicha qidirish
#  Eng yaqin klinikalar ro'yxatini chiqarish Bosh sahifaga qaytish
def user_search_cbuttons(search_clinic: str, search_doctor: str, search_address: str, nearest_clinics: str,
                         back_main_menu: str):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"🏥 {search_clinic}")
            ],
            [
                KeyboardButton(text=f"💉 {search_doctor}")
            ],
            [
                KeyboardButton(text=f"📍 {search_address}")
            ],
            [
                KeyboardButton(text=f"🚶‍♂️ {nearest_clinics}")
            ],
            [
                KeyboardButton(text=f"🏡 {back_main_menu}")
            ],
        ]
    )
    return buttons
