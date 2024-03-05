from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.clinics import doctors


def select_gender_communicate():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👨‍⚕️ Erkak shifokor", callback_data="communicate_Erkak")
            ],
            [
                InlineKeyboardButton(text="👩‍⚕️ Ayol shifokor", callback_data="communicate_Ayol")
            ],
            [
                InlineKeyboardButton(text="💊 Farqi yo'q", callback_data="communicate_Farqsiz")
            ],
            [
                InlineKeyboardButton(text="⬅️ Ortga", callback_data="back_main_user")
            ]
        ]
    )
    return keyboard


def user_select_doctors_ibutton():
    builder = InlineKeyboardBuilder()

    for doctor in doctors:
        builder.button(text=doctor, callback_data=f"communicatedoctors_{doctor}")
    builder.adjust(3)
    builder.row(InlineKeyboardButton(text="⬅️ Ortga", callback_data="back_communicate"))
    return builder.as_markup()


def user_send_complaint():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔄 Qayta kiritish", callback_data="re_enter_communicate"),
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="check_communicate")
            ],
            [
              InlineKeyboardButton(text="⬅️ Ortga", callback_data="back_communicate")
            ]
        ]
    )
    return keyboard
