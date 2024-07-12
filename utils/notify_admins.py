import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "<b>🏃 Bot Started...</b>")

        except Exception as err:
            logging.exception(f"{err} | ID : {admin}")


async def on_shutdown_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "<b>Bot Stopped 🛑</b>")
        except Exception as err:
            logging.exception(f"{err} | ID : {admin}")
