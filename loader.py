import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from data import config
from utils.API.Users.get import UsersGet
# from utils.API.get import UsersGet
# from utils.API.post import UserPoster
# from utils.API.put import UserDataUpdater
# from utils.PostgreSQL.postgres import Database
# from utils.sqlite3.Class import Database_SQLITE

BASE_DIR = Path(__file__).resolve().parent.parent
# db = Database()
get = UsersGet()
# post = UserPoster()
# put = UserDataUpdater()
# sqlt_db = Database_SQLITE(path_to_db="data/keyboards.db")

loop = asyncio.new_event_loop()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
