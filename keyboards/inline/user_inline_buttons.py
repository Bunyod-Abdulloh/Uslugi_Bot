from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.clinics import doctors


def select_gender_communicate(man_text: str, man_callback: str, woman_text, woman_callback, back_text,
                              back_callback, all_text, all_callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"👨‍⚕️ {man_text}", callback_data=man_callback)
            ],
            [
                InlineKeyboardButton(text=f"👩‍⚕️ {woman_text}", callback_data=woman_callback)
            ],
            [
                InlineKeyboardButton(text=f"💊 {all_text}", callback_data=all_callback)
            ],
            [
                InlineKeyboardButton(text=f"⬅️ {back_text}", callback_data=back_callback)
            ]
        ]
    )
    return keyboard


def user_select_doctors_ibutton(callback: str, back_text: str, back_callback):
    builder = InlineKeyboardBuilder()

    for doctor in doctors:
        builder.button(text=doctor, callback_data=f"{callback}_{doctor}")
    builder.adjust(3)
    builder.row(InlineKeyboardButton(text=f"⬅️ {back_text}", callback_data=back_callback))
    return builder.as_markup()


def user_send_complaint(re_enter_text: str, re_enter_callback, check_text: str, check_callback: str,
                        back_text: str, back_callback: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"🔄 {re_enter_text}", callback_data=re_enter_callback),
                InlineKeyboardButton(text=f"✅ {check_text}", callback_data=check_callback)
            ],
            [
              InlineKeyboardButton(text=f"⬅️ {back_text}", callback_data=back_callback)
            ]
        ]
    )
    return keyboard