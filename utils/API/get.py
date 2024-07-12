import aiohttp

from data.config import DJANGO_USERS_API, DJANGO_TOP_USERS_API


class UsersGet:
    def __init__(self):
        self.get_api_user = DJANGO_USERS_API
        self.get_api_top_users = DJANGO_TOP_USERS_API

    async def get_users(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.get_api_user) as info_users:
                    if info_users.status == 200:
                        data = await info_users.json()
                        if str(data) == '[]':
                            return None
                        return data
                    else:
                        return False
        except aiohttp.ClientConnectionError:
            return "Error"

    async def get_user(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_personal_data(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/personal-data") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_is_admin(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/permissions") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_first_name(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/first-name") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_last_name(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/last-name") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_region(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/region") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_district(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/district") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_phone_number(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/phone-number") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_scores(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/scores") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_is_ban(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/ban") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_user_is_active(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/active/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_olimpiada(self, tg_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_user}/{tg_id}/active/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_top_users(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_top_users}/top-users/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_next_top_users(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_top_users}/next-top-users/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_excel_olimpiada(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_top_users}/excel-olimpiada-users/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_excel_no_olimpiada(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_top_users}/excel-no-olimpiada-users/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False

    async def get_count_users(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.get_api_top_users}/count-users/") as info_user:
                if info_user.status in [400, 404]:
                    return None
                else:
                    if info_user.status == 200:
                        return await info_user.json()
                    else:
                        return False
