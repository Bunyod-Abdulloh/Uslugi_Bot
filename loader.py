from aiogram import Bot, Dispatcher
from data import config
from utils.database.postgresql import Database

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()
db = Database()

