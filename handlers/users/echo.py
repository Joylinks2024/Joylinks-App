from aiogram import types

from data.config import CHANNELS_IDS
from keyboards.inline.create.main_create_inl import create_check_sup_inl
from loader import dp, bot
from utils.channels.main_check import check, filter_channels


@dp.message_handler(state=None)
async def filter_text(message: types.Message):
    status = await check(user_id=message.chat.id, channels=CHANNELS_IDS)
    if not status:
        ...
    else:
        info_channel = await filter_channels(user_id=message.chat.id, bot=bot)
        await message.answer(info_channel[0], disable_web_page_preview=True,
                             reply_markup=await create_check_sup_inl(title=info_channel[1],
                                                                     invite_links=info_channel[2]))
