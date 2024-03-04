from aiogram import types, Router
from aiogram.filters import CommandStart

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Klinika botimizga xush kelibsiz!')


# @dp.message()
# async def echo(message: types.Message):
#     text = message.text
#
#     if text in ['Привет', 'привет', 'hi', 'hello']:
#         await message.answer('И тебе привет!')
#     elif text in ['Пока', 'пока', 'До свидания']:
#         await message.answer('И тебе пока!')
#     else:
#         await message.answer(message.text)

