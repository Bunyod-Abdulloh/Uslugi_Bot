from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_default_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Mutaxassis bilan bog'lanish")
        ],
        [
            KeyboardButton(text="🔍 Tibbiy hizmat turi bo'yicha qidirish")
        ],
        [
            KeyboardButton(text="📍 Manzil bo'yicha qidirish")
        ],
        [
            KeyboardButton(text="👤 Shaxsiy kabinet")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
