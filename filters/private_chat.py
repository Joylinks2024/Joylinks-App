from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, ChatType


class ChatPrivateFilter(BoundFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
