# import aiohttp
#
# from data.config import DJANGO_USERS_API
#
#
# class UserPoster:
#     def __init__(self):
#         self.post_user_info = f"{DJANGO_USERS_API}/"
#
#     async def post_user(self, telegram_id, first_name, last_name, tg_full_name,
#                         tg_username, region, district, phone_number):
#         post_json = {"telegram_id": telegram_id,
#                      "first_name": first_name,
#                      "last_name": last_name,
#                      "tg_full_name": tg_full_name,
#                      "tg_username": tg_username,
#                      "region": region,
#                      "district": district,
#                      "phone_number": phone_number}
#         async with aiohttp.ClientSession() as session:
#             async with session.post(url=self.post_user_info, json=post_json) as response:
#                 return response
