from aiogram import types
from aiogram.types import ParseMode

from data.config import CHANNELS_IDS
# from keyboards.default.create_defoult.main_create_btn import start_btn, super_admin, \
#     admin_buyurtmalar_bolim
from keyboards.inline.create.main_create_inl import create_check_sup_inl
# from keyboards.inline.create.savol_javob import create_web_bage
from loader import dp, get, bot
# from states.create_states.main_state import Save_Users_Info
from utils.channels.main_check import check, filter_channels
from utils.extra_datas import make_html


@dp.message_handler(commands=['start', 'restart'])
async def bot_start(message: types.Message):
    a = await get.get_user(tg_id=message.chat.id)
    await message.answer(a)


# @dp.message_handler(commands=['start', 'restart'])
# async def bot_start_users(message: types.Message):
#     tg_id = message.chat.id
#     text_is_active = ""
#     user = await get.get_user(tg_id=tg_id)
#     if user is None:
#         await Save_Users_Info.name.set()
#         await message.answer(f"<b>Assalomu alaykum. Ushbu bot orqali \"Joylinks IT academy\" "
#                              f"haqida bilib olishingiz mumkin.</b>\n\n"
#                              f"<i>Botdan foydalanish uchun iltimos ismingizni yozib yuboring.</i>",
#                              parse_mode=ParseMode.HTML)
#     else:
#         status = await check(user_id=message.chat.id, channels=CHANNELS_IDS)
#         if not status:
#             if user['is_active'] == False:
#                 info_db = await put.put_is_active(tg_id=message.chat.id)
#                 if info_db is True:
#                     text_is_active = "\n\n<b><i>Qaytganingiz bilan</i></b>"
#                 elif info_db is None:
#                     await Save_Users_Info.name.set()
#                     return await message.answer(f"<b>Assalomu alaykum. Ushbu bot orqali \"Joylinks IT academy\" "
#                                                 f"haqida bilib olishingiz mumkin.</b>\n\n"
#                                                 f"<i>Botdan foydalanish uchun iltimos ismingizni yozib yuboring.</i>",
#                                                 parse_mode=ParseMode.HTML)
#             if user['is_ban'] == True:
#                 return await message.answer(f"<b>Siz Admin tomonidan bloklangansiz</b>{text_is_active}",
#                                             reply_markup=types.ReplyKeyboardRemove())
#             if user['is_superadmin'] == True:
#                 url = "https://joylinks-django-bot.onrender.com/admin/"
#                 await message.answer("Web App", reply_markup=await create_web_bage(url=url))
#                 return await message.answer(
#                     f"<b>Assalomalaykum hurmatli {make_html(user['first_name'])}</b>{text_is_active}",
#                     reply_markup=await super_admin())
#             if user['is_admin'] == True:
#                 return await message.answer(
#                     f"<b>Assalomalaykum hurmatli {make_html(user['first_name'])}</b>{text_is_active}",
#                     reply_markup=await admin_buyurtmalar_bolim())
#             return await message.answer(
#                 f"<b>Assalomalaykum hurmatli {make_html(user['first_name'])}</b>{text_is_active}",
#                 reply_markup=await start_btn(), parse_mode=ParseMode.HTML)
#         else:
#             info_channel = await filter_channels(user_id=message.chat.id, bot=bot)
#             await message.answer(info_channel[0], disable_web_page_preview=True,
#                                  reply_markup=await create_check_sup_inl(title=info_channel[1],
#                                                                          invite_links=info_channel[2]))
