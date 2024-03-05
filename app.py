import asyncio
import logging
import sys

from aiogram import Dispatcher, Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.middlewares.request_logging import logger
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data.config import BOT_TOKEN
from handlers.users.start import user_start_router
from handlers.users.user_communicate import user_communicate_router
from handlers.users.user_main import user_main_router
from loader import db
from middlewares.throttling import ThrottlingMiddleware
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def setup_handlers(dp: Dispatcher) -> None:
    """HANDLERS"""
    dp.include_router(user_start_router)
    dp.include_router(user_main_router)
    dp.include_router(user_communicate_router)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dp=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    logger.info("Configured aiogram")


async def database_connected():
    await db.create()
    # await db.drop_users()
    await db.drop_table_complaint()
    await db.create_table_users()
    await db.create_table_complaint()


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Database connected")
    await database_connected()

    logger.info(msg="Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)
    allowed_updates = ['message', 'callback_query']
    dispatcher.startup.register(aiogram_on_startup_polling)
    dispatcher.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dispatcher.start_polling(bot, close_bot_session=True, allowed_updates=allowed_updates))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped!")
