from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS_IDS
from keyboards.inline.create.main_create_inl import create_check_sup_inl
from loader import bot
from utils.channels.main_check import check


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query.from_user.id:
            user = update.callback_query.from_user.id
        else:
            return
        results = "Botdan foydalanish uchun quidagi kanallarga obuna bo'ling:\n"
        channel_ids = []
        chanel_names = []
        final_status = True
        status = check(user_id=user,
                       channels=CHANNELS_IDS)
        final_status *= status
        channel = await bot.get_chat(CHANNELS_IDS)
        if not status:
            invite_link = await channel.export_invite_link()
            results += (f"👉🏻 <a href='{invite_link}'> {channel.title}</a>\n")
            channel_ids.append(invite_link)
            chanel_names.append(channel.title)

        if not final_status:
            await update.message.answer(results, disable_web_page_preview=True,
                                        reply_markup=await create_check_sup_inl(title=chanel_names,
                                                                                invite_links=channel_ids))
            raise CancelHandler()
