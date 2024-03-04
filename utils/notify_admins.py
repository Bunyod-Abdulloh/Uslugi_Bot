import logging

from aiogram import Dispatcher

from app import bot
from data.config import ADMINS


# async def on_startup_notify(dp: Dispatcher):
#     for admin in ADMINS:
#         try:
#             await dp.send_message(admin, "Bot ishga tushdi")
#         except Exception as err:
#             logging.exception(err)
