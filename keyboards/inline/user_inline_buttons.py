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


def user_search_ibuttons(search_clinic: str, search_doctor: str, search_address: str, nearest_clinics: str,
                         back_main_menu: str):
    buttons = InlineKeyboardMarkup(
        inline_keyboard =[
            [
                InlineKeyboardButton(text=f"🏥 {search_clinic}", callback_data=search_clinic,
                                     switch_inline_query="salom")
            ],
            [
                InlineKeyboardButton(text=f"💉 {search_doctor}", callback_data=search_doctor)
            ],
            [
                InlineKeyboardButton(text=f"📍 {search_address}", callback_data=search_address)
            ],
            [
                InlineKeyboardButton(text=f"🚶‍♂️ {nearest_clinics}", callback_data=nearest_clinics)
            ],
            [
                InlineKeyboardButton(text=f"⬅️ {back_main_menu}", callback_data="ortga")
            ],
        ]
    )
    return buttons
