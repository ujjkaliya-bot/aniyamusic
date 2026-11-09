# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ANIYAXMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=f"❌ {_[\"CLOSE_BUTTON\"]}", callback_data="close")]
    second = [
        InlineKeyboardButton(text=f"⬅️ {_[\"BACK_PAGE\"]}", callback_data="mbot_cb"),
        InlineKeyboardButton(text=f"🔙 {_[\"BACK_BUTTON\"]}", callback_data="settingsback_helper"),
        InlineKeyboardButton(text=f"{_[\"NEXT_PAGE\"]} ➡️", callback_data="mbot_cb"),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=f"👑 {_[\"H_B_1\"]}", callback_data="help_callback hb1"),
                InlineKeyboardButton(text=f"🔐 {_[\"H_B_2\"]}", callback_data="help_callback hb2"),
                InlineKeyboardButton(text=f"🎙️ {_[\"H_B_3\"]}", callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(text=f"💬 {_[\"H_B_4\"]}", callback_data="help_callback hb4"),
                InlineKeyboardButton(text=f"👥 {_[\"H_B_5\"]}", callback_data="help_callback hb5"),
                InlineKeyboardButton(text=f"🎵 {_[\"H_B_6\"]}", callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(text=f"🚫 {_[\"H_B_7\"]}", callback_data="help_callback hb7"),
                InlineKeyboardButton(text=f"🔁 {_[\"H_B_8\"]}", callback_data="help_callback hb8"),
                InlineKeyboardButton(text=f"📜 {_[\"H_B_9\"]}", callback_data="help_callback hb9"),
            ],
            [
                InlineKeyboardButton(text=f"📡 {_[\"H_B_10\"]}", callback_data="help_callback hb10"),
                InlineKeyboardButton(text=f"▶️ {_[\"H_B_11\"]}", callback_data="help_callback hb11"),
                InlineKeyboardButton(text=f"🔀 {_[\"H_B_12\"]}", callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text=f"⏩ {_[\"H_B_13\"]}", callback_data="help_callback hb13"),
                InlineKeyboardButton(text=f"🎧 {_[\"H_B_14\"]}", callback_data="help_callback hb14"),
                InlineKeyboardButton(text=f"⚡ {_[\"H_B_15\"]}", callback_data="help_callback hb15"),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=f"🔙 {_[\"BACK_BUTTON\"]}", callback_data="settings_back_helper")]]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"❔ {_[\"S_B_4\"]}",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
