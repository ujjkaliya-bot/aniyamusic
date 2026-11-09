# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ANIYAXMUSIC import LOGGER, app, userbot
from ANIYAXMUSIC.core.call import ANIYA
from ANIYAXMUSIC.misc import sudo
from ANIYAXMUSIC.plugins import ALL_MODULES
from ANIYAXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    app_started = False
    userbot_started = False
    call_started = False

    try:
        if not any((config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5)):
            LOGGER(__name__).error(
                "String session not filled. Configure at least one assistant session."
            )
            return

        await sudo()
        try:
            for user_id in await get_gbanned():
                BANNED_USERS.add(user_id)
            for user_id in await get_banned_users():
                BANNED_USERS.add(user_id)
        except Exception as exc:
            LOGGER(__name__).warning(
                f"Could not load all banned users: {type(exc).__name__}"
            )

        await app.start()
        app_started = True

        for all_module in ALL_MODULES:
            importlib.import_module("ANIYAXMUSIC.plugins" + all_module)
        LOGGER("ANIYAXMUSIC.plugins").info("All features loaded.")

        await userbot.start()
        userbot_started = True

        await ANIYA.start()
        call_started = True

        try:
            await ANIYA.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
        except NoActiveGroupCall:
            LOGGER("ANIYAXMUSIC").warning(
                "No active voice chat was found in LOGGER_ID. Startup will continue."
            )
        except Exception as exc:
            LOGGER("ANIYAXMUSIC").warning(
                f"Startup voice-chat test was skipped: {type(exc).__name__}"
            )

        await ANIYA.decorators()
        LOGGER("ANIYAXMUSIC").info("AniyaMusic is running.")
        await idle()

    finally:
        # Each service is stopped independently: one shutdown error must not
        # prevent the remaining Telegram/PyTgCalls clients from closing.
        if call_started:
            try:
                await ANIYA.stop()
            except Exception as exc:
                LOGGER("ANIYAXMUSIC").warning(
                    f"Voice-call shutdown warning: {type(exc).__name__}"
                )
        if userbot_started:
            try:
                await userbot.stop()
            except Exception as exc:
                LOGGER("ANIYAXMUSIC").warning(
                    f"Assistant shutdown warning: {type(exc).__name__}"
                )
        if app_started:
            try:
                await app.stop()
            except Exception as exc:
                LOGGER("ANIYAXMUSIC").warning(
                    f"Bot shutdown warning: {type(exc).__name__}"
                )
        LOGGER("ANIYAXMUSIC").info("AniyaMusic shutdown complete.")


if __name__ == "__main__":
    asyncio.run(init())
