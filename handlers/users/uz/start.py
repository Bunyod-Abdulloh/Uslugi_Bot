from aiogram import types, Router
from aiogram.filters import CommandStart

from keyboards.default.user_default_buttons import user_main_default_button

user_start_router = Router()

uz_main_keyboard = user_main_default_button(
    communicate_doctor="Shifokor bilan bog'lanish", search="Qidirish", profile="Shaxsiy kabinet"
)


@user_start_router.message(CommandStart())
async def start_cmduz(message: types.Message):
    await message.answer(
        text='Klinika botimizga xush kelibsiz!',
        reply_markup=uz_main_keyboard
    )
