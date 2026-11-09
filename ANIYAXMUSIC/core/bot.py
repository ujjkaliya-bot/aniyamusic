# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class ANIYA(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="TIDALXMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        if config.LOGGER_ID:
            try:
                await self.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\\n\\nɪᴅ : <code>{self.id}</code>\\nɴᴀᴍᴇ : {self.name}\\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
                )
                member = await self.get_chat_member(config.LOGGER_ID, self.id)
                if member.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).warning("LOGGER_ID channel: promote the bot as admin to enable log notifications.")
            except Exception as ex:
                LOGGER(__name__).warning(
                    f"Logger channel unavailable; bot will continue without log notifications ({type(ex).__name__})."
                )
        else:
            LOGGER(__name__).warning("LOGGER_ID is not configured; log notifications are disabled.")
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
