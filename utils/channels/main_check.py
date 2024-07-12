from typing import Union

from aiogram import Bot

from data.config import CHANNELS_IDS


async def check(user_id, channels: Union[str, int, list]):
    bot = Bot.get_current()
    is_sup = []
    for channel in channels:
        member = await bot.get_chat_member(user_id=user_id, chat_id=channel.strip())
        if member.is_chat_member() is False: is_sup.append(member.is_chat_member())
    return is_sup


async def filter_channels(user_id, bot: Bot, text=None):
    if text is not None:
        results = f"{text}\n\n"
    else:
        results = "<b>Botdan foydalanish uchun quidagi kanallarga obuna bo'ling:</b>\n\n"
    title = []
    invite_links = []
    for channel_id in CHANNELS_IDS:
        member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id.strip())
        if not member.is_chat_member():
            channel = await bot.get_chat(channel_id.strip())
            invite_link = await channel.export_invite_link()
            results += f"👉🏻 <a href='{invite_link}'> {channel.title}</a>\n"
            title.append(channel.title)
            invite_links.append(invite_link)
    return results, title, invite_links
