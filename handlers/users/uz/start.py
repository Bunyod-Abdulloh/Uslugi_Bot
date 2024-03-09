from aiogram import types, Router
from aiogram.filters import CommandStart

from keyboards.default.user_default_buttons import user_main_default_button

user_start_router = Router()

uz_main_keyboard = user_main_default_button(
    communicate_doctor="Shifokor bilan bog'lanish", search="Qidirish", profile="Shaxsiy kabinet"
)


@user_start_router.message(CommandStart())
async def start_cmduz(message: types.Message):
    # buttons = types.ReplyKeyboardMarkup(
    #     keyboard=[
    #         [
    #             types.KeyboardButton(text="🛍 Mahsulotlar")
    #         ],
    #         [
    #             types.KeyboardButton(text="👤 Shaxsiy kabinet"),
    #             types.KeyboardButton(text="🛒 Savat")
    #         ],
    #         [
    #             types.KeyboardButton(text="❓ Savol yuborish")
    #         ],
    #         [
    #             types.KeyboardButton(text="📰 Foydali maqolalar")
    #         ]
    #     ],
    #     resize_keyboard=True
    # )
    print(message.from_user.id)
    await message.answer(
        text='Botimizga xush kelibsiz!',
        reply_markup=uz_main_keyboard
    )
