from aiogram import types, Router
from aiogram.filters import CommandStart

user_start_router = Router()


@user_start_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Klinika botimizga xush kelibsiz!')
