# import asyncio
# import logging
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
#
# from data.config import ADMINS, CHANNELS_IDS
# from keyboards.default.create_defoult.main_create_btn import super_admin, go_home, super_send_message
# from keyboards.inline.create.buttons import are_you_sure_markup
# from loader import db, bot, dp, get
# from states.create_states.test import AdminState
# from utils.extra_datas import make_html
# from utils.pgtoexcel import export_to_excel
#
#
# @dp.message_handler(Command('allusers'))
# async def get_all_users(message: types.Message):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] is True:
#         if info_db['is_ban'] is True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         users = await db.select_all_users_for_xlsx()
#         print(users)
#         # file_path = f"data/joylinks_users.xlsx"
#         # await export_to_excel(data=users,
#         #                       headings=['ID', 'Ism', 'Familya', 'Telegram Ism', 'Telegram User Name',
#         #                                 'Viloyat', 'Tuman', 'Telefon Raqam', 'Jami Ball',
#         #                                 'Telegram ID', 'Activ Holat'],
#         #                       filepath=file_path)
#         # await message.answer_document(types.input_file.InputFile(file_path))
#
#
# @dp.message_handler(Command('reklama'))
# async def ask_ad_content(message: types.Message):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] is True:
#         if info_db['is_ban'] is True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         await message.answer("<b>Bo'limni Tanlang</b>", reply_markup=await super_send_message())
#
#
# @dp.message_handler(state=AdminState.ask_ad_content)
# async def send_ad_to_users(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] is True:
#         if info_db['is_ban'] is True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         if message.text in ["⬅ Orqaga", "/start"]:
#             await state.finish()
#             await message.answer(f"<b>Assalomalaykum hurmatli {make_html(info_db['name'])}</b>",
#                                  reply_markup=await super_admin())
#         elif message.text == "/help":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML",
#                                  reply_markup=await go_home())
#         else:
#             users = await db.select_all_users()
#             count = 0
#             for user in users:
#                 user_id = user[-1]
#                 try:
#                     await message.send_copy(chat_id=user_id)
#                     count += 1
#                     await asyncio.sleep(0.05)
#                 except Exception as error:
#                     logging.info(f"Ad did not send to user: {user_id}. Error: {error}")
#             await message.answer(f"<b>Reklama {count} ta foydalauvchiga muvaffaqiyatli yuborildi.</b>",
#                                  parse_mode="HTML")
#             await state.finish()
#
#
# @dp.message_handler(state=AdminState.send_ad_chanel_user)
# async def send_ad_to_chanel_and_user(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] is True:
#         if info_db['is_ban'] is True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         if message.text in ["⬅ Orqaga", "/start"]:
#             await state.finish()
#             await message.answer(f"<b>Assalomalaykum hurmatli {make_html(info_db['name'])}</b>",
#                                  reply_markup=await super_admin())
#         elif message.text == "/help":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML",
#                                  reply_markup=await go_home())
#         else:
#             users = await db.select_all_users()
#             count = 0
#             await message.send_copy(chat_id=CHANNEL_ID)
#             await asyncio.sleep(0.05)
#             for user in users:
#                 user_id = user[-1]
#                 try:
#                     await message.send_copy(chat_id=user_id)
#                     count += 1
#                     await asyncio.sleep(0.05)
#                 except Exception as error:
#                     logging.info(f"Ad did not send to user: {user_id}. Error: {error}")
#             await message.answer(
#                 f"<b>Reklama {count} ta foydalauvchiga va 1 ta kanalga muvaffaqiyatli yuborildi.</b>",
#                 parse_mode="HTML")
#             await state.finish()
#
#
# @dp.message_handler(state=AdminState.send_ad_chanel)
# async def send_ad_to_chanel(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] is True:
#         if info_db['is_ban'] is True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         if message.text in ["⬅ Orqaga", "/start"]:
#             await state.finish()
#             await message.answer(f"<b>Assalomalaykum hurmatli {make_html(info_db['name'])}</b>",
#                                  reply_markup=await super_admin())
#         elif message.text == "/help":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML",
#                                  reply_markup=await go_home())
#         else:
#             await message.send_copy(chat_id=CHANNEL_ID)
#             await message.answer(f"<b>Reklama 1 ta kanalga muvaffaqiyatli yuborildi.</b>",
#                                  parse_mode="HTML", reply_markup=await super_admin())
#             await state.finish()
#
#
# @dp.message_handler(state=AdminState.get_id)
# async def send_ad_to_chanel(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] == True:
#         if info_db['is_ban'] == True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         if message.text.isdigit():
#             await state.update_data({
#                 "ad_user_id": message.text
#             })
#             await state.set_state(AdminState.send_ad_user)
#             await message.answer("<b>Xabaringiz Yuboring ...</b>")
#
#
# @dp.message_handler(state=AdminState.get_id)
# async def send_ad_to_chanel(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] == True:
#         if info_db['is_ban'] == True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         try:
#             data = await state.get_data()
#             user_id = data["ad_user_id"]
#             await message.send_copy(chat_id=user_id)
#             await state.finish()
#             await message.answer("<b>Xabaringiz Yuborildi ✅</b>")
#         except:
#             if message.text in ["⬅ Orqaga", "/start"]:
#                 await message.answer(f"<b>Assalomalaykum hurmatli {make_html(info_db['name'])}</b>",
#                                      reply_markup=await super_admin())
#             elif message.text == "/help":
#                 await message.answer("<b>ID ni Kiriting</b>", parse_mode="HTML", reply_markup=await go_home())
#             else:
#                 await state.finish()
#                 await message.answer("<b>Xabaringiz Yuborilmadi ❌\n\n"
#                                      "<i>ID ni tekshirib qayta urinib ko'ring</i></b>",
#                                      reply_markup=await super_admin())
#
#
# @dp.message_handler(Command('cleandb'), chat_id=ADMINS)
# async def ask_are_you_sure(message: types.Message, state: FSMContext):
#     msg = await message.reply("<b>Haqiqatdan ham bazani tozalab yubormoqchimisiz?</b>",
#                               reply_markup=are_you_sure_markup, parse_mode="HTML")
#     await state.update_data(msg_id=msg.message_id)
#     await state.set_state(AdminState.are_you_sure)
#
#
# @dp.callback_query_handler(state=AdminState.are_you_sure, chat_id=ADMINS)
# async def clean_db(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg_id = data.get('msg_id')
#     if call.data == 'yes':
#         await db.delete_users()
#         text = "Baza tozalandi!"
#     elif call.data == 'no':
#         text = "Bekor qilindi."
#     else:
#         text = "Nomalum buyruq"
#     await bot.edit_message_text(text=f"<b>{text}</b>", chat_id=call.message.chat.id, message_id=msg_id)
#     await state.finish()
#
#
# send_message_btn = [
#     "Botga Yuborish 🤖",
#     "Kanalga Yuborish 🔈",
#     "Kanal va Botga Yuborish",
#     "1️⃣ Foydalanuvchiga 👤"
# ]
#
#
# @dp.message_handler(text=send_message_btn)
# async def info_admins(message: types.Message, state: FSMContext):
#     info_db = await get.get_user(tg_id=message.chat.id)
#     if info_db['is_superadmin'] == True:
#         if info_db['is_ban'] == True:
#             return await message.answer("<b>Siz Admin tomonidan bloklangansiz</b>",
#                                         reply_markup=types.ReplyKeyboardRemove())
#         if message.text == "Botga Yuborish 🤖":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML", reply_markup=await go_home())
#             await state.set_state(AdminState.ask_ad_content)
#         elif message.text == "Kanalga Yuborish 🔈":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML", reply_markup=await go_home())
#             await state.set_state(AdminState.send_ad_chanel)
#         elif message.text == "Kanal va Botga Yuborish":
#             await message.answer("<b>Reklama uchun post yuboring</b>", parse_mode="HTML", reply_markup=await go_home())
#             await state.set_state(AdminState.send_ad_chanel_user)
#         elif message.text == "1️⃣ Foydalanuvchiga 👤":
#             await message.answer("<b>ID ni Kiriting</b>", parse_mode="HTML", reply_markup=await go_home())
#             await state.set_state(AdminState.get_id)
