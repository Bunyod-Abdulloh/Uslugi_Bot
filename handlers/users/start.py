from aiogram import types, Router
from aiogram.filters import CommandStart

from keyboards.default.user_default_buttons import user_main_default_button

user_start_router = Router()


# Hi bro, how are you :)

@user_start_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        text='Klinika botimizga xush kelibsiz!',
        reply_markup=user_main_default_button
    )
