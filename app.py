import asyncio
from aiogram import Bot, Dispatcher, types

from data.config import BOT_TOKEN
from handlers.users.start import user_start_router
from handlers.users.user_communicate import user_communicate_router
from handlers.users.user_main import user_main_router
from utils.set_bot_commands import private

ALLOWED_UPDATES = ['message, callback_query, inline_query']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_start_router)
dp.include_router(user_main_router)
dp.include_router(user_communicate_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(
        commands=private,
        scope=types.BotCommandScopeAllPrivateChats()
    )
    # await on_startup_notify()
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
