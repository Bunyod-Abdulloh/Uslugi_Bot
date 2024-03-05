from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from data import config
from utils.database.postgresql import Database

dp = Dispatcher()
db = Database()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
