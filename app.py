import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from data.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Klinika botimizga xush kelibsiz!')


@dp.message()
async def echo(message: types.Message):
    text = message.text

    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer('И тебе пока!')
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
