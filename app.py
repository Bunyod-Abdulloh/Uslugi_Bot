import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.middlewares.request_logging import logger
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data.config import BOT_TOKEN
from handlers.users.uz.search_clinics import clinics_router, uz_back_search_router
from handlers.users.uz.start import user_start_router
from handlers.users.uz.communicate import user_complaint_router
from handlers.users.uz.main import user_main_router
from handlers.users.uz.search_main import search_router
from loader import db
from middlewares.throttling import ThrottlingMiddleware
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    dispatcher.include_routers(user_start_router, user_main_router, user_complaint_router, search_router)
    dispatcher.include_routers(clinics_router, uz_back_search_router)


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    # logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    # logger.info("Configured aiogram")


async def database_connected():
    await db.create()
    # await db.drop_users()
    # await db.drop_table_complaint()
    await db.create_table_users()
    await db.create_table_complaint()
    await db.create_table_company()


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info(msg="Start polling!")
    await database_connected()

    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    # logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)
    allowed_updates = ['message', 'callback_query', 'inline_query', 'chosen_inline_result']
    dispatcher.startup.register(aiogram_on_startup_polling)
    dispatcher.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dispatcher.start_polling(bot, close_bot_session=True,
                                         allowed_updates=allowed_updates))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped!")
