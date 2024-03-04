from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.clinics import doctors


def user_select_doctors_ibutton():
    builder = InlineKeyboardBuilder()

    for doctor in doctors:
        builder.button(text=doctor, callback_data=f'communicate_{doctor}')
    builder.adjust(3)
    return builder.as_markup()
