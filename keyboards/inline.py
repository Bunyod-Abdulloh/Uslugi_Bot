from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.clinics import doctors


def user_select_doctors_ibutton():
    builder = InlineKeyboardBuilder()

    for doctor in doctors:
        builder.button(text=doctor, callback_data=doctor)
    return builder
