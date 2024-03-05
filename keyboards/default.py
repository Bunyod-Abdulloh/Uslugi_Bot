from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_default_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Shifokor bilan bog'lanish")
        ],
        [
            KeyboardButton(text="🔍 Qidirish")
        ],
        [
            KeyboardButton(text="👤 Shaxsiy kabinet")
        ]
    ],
    resize_keyboard=True
)


user_search_cbuttons = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="🏥 Klinika bo'yicha qidirish")
        ],
        [
          KeyboardButton(text="💉 Shifokor sohasi bo'yicha qidirish")
        ],
        [
            KeyboardButton(text="📍 Manzil bo'yicha qidirish")
        ],
        [
          KeyboardButton(text="🚶‍♂️ Eng yaqin klinikalarni chiqarish")
        ],
        [
          KeyboardButton(text="🏡 Bosh sahifaga qaytish")
        ],
    ]
)
