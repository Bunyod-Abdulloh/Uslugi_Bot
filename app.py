import asyncio
from aiogram import Bot, Dispatcher

from data.config import BOT_TOKEN
from handlers.users.start import user_private_router

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
