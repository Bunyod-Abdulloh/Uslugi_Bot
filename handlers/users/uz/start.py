from aiogram import types, Router
from aiogram.filters import CommandStart

from keyboards.default.user_default_buttons import user_main_default_button

router = Router()

uz_main_keyboard = user_main_default_button(
    communicate_doctor="Shifokor bilan bog'lanish", search="Qidirish", profile="Shaxsiy kabinet"
)


@router.message(CommandStart())
async def start_cmduz(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        text='Botimizga xush kelibsiz!',
        reply_markup=uz_main_keyboard
    )
