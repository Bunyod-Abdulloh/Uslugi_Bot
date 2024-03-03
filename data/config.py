from environs import Env

env = Env()
env.read_env()


ADMINS = env.list("ADMINS")
BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
