from aiogram import executor

from loader import dp
from utils.misc.logging import logger
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands

import middlewares, filters, handlers


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    # await avto_restarter()


async def on_shutdown(dispatcher):
    # Bot ishdan to'xtagani haqida adminga xabar berish
    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    logger.info("Stop Bot")
    logger.info("Closed DB")
