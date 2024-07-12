import aiohttp

from data.config import DJANGO_USERS_API


class UserDataUpdater:
    def __init__(self):
        self.api_url = DJANGO_USERS_API

    async def put_data(self, url, put_info):
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=put_info) as response:
                return response.status == 200

    async def first_name(self, tg_id: int, first_name: str):
        """
        :param tg_id: iteger
        :param first_name: string
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/first-name/"
        put_info = {"first_name": first_name}
        return await self.put_data(url, put_info)

    async def last_name(self, tg_id: int, last_name: str):
        """
        :param tg_id: iteger
        :param last_name: string
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/last-name/"
        put_info = {"last_name": last_name}
        return await self.put_data(url, put_info)

    async def region(self, tg_id: int, region: str):
        """
        :param tg_id: iteger
        :param region: string
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/region/"
        put_info = {"region": region}
        return await self.put_data(url, put_info)

    async def district(self, tg_id: int, district: str, region: str):
        """
        :param tg_id: iteger
        :param district: string
        :return: if save True, elif user not found returning 'None', else False
        """
        await self.region(tg_id=tg_id, region=region)
        url = f"{self.api_url}/{tg_id}/district/"
        put_info = {"district": district}
        return await self.put_data(url, put_info)

    async def phone_number(self, tg_id: int, phone_number: [int, str]):
        """
        :param tg_id: iteger
        :param phone_number: iteger, string
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/phone-number/"
        put_info = {"phone_number": phone_number}
        return await self.put_data(url, put_info)

    async def put_is_active(self, tg_id: int, is_active: bool = True):
        """
        :param tg_id: iteger
        :param is_active: bool defoult True
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/active/"
        put_info = {"is_active": is_active}
        return await self.put_data(url, put_info)

    async def put_is_ban(self, tg_id: int, is_ban: bool = False):
        """
        :param tg_id: iteger
        :param is_ban: bool defoult False
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/ban/"
        put_info = {"is_ban": is_ban}
        return await self.put_data(url, put_info)

    async def put_is_admin(self, tg_id: int, is_superadmin: bool = False, is_admin: bool = False):
        """
        :param tg_id: iteger
        :param is_superadmin: bool defoult False
        :param is_admin: bool defoult False
        :return: if save True, elif user not found returning 'None', else False
        """
        await self.put_is_ban(tg_id=tg_id, is_ban=False)
        url = f"{self.api_url}/{tg_id}/permissions/"
        put_info = {"is_superadmin": is_superadmin,
                    "is_admin": is_admin}
        return await self.put_data(url, put_info)

    async def put_score(self, tg_id: int, math_score: int, english_score: int, iq_score: int, total_score: int):
        """
        :param tg_id: iteger
        :param math_score: iteger
        :param english_score: iteger
        :param iq_score: iteger
        :param total_score: iteger max 100
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/scores/"
        put_info = {"math_score": math_score,
                    "english_score": english_score,
                    "iq_score": iq_score,
                    "total_score": total_score}
        return await self.put_data(url, put_info)

    async def put_olimpiada(self, tg_id: int, olimpiada: bool = True):
        """
        :param tg_id: iteger
        :param olimpiada: boolian
        :return: if save True, elif user not found returning 'None', else False
        """
        url = f"{self.api_url}/{tg_id}/olimpiada/"
        put_info = {"olimpiada": olimpiada}
        return await self.put_data(url, put_info)
