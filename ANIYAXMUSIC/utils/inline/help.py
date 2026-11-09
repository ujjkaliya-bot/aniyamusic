# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# AniyaMusic — High-Performance Telegram Voice Chat Music & Video Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ANIYAXMUSIC import app


def _button(text, callback_data, style):
    # Telegram Bot API 9.4 supports primary (blue), success (green), danger (red).
    return {"text": text, "callback_data": callback_data, "style": style}


def help_pannel(_, START: Union[bool, int] = None):
    rows = [
        [
            _button(_["H_B_1"], "help_callback hb1", "primary"),
            _button(_["H_B_2"], "help_callback hb2", "success"),
            _button(_["H_B_3"], "help_callback hb3", "danger"),
        ],
        [
            _button(_["H_B_4"], "help_callback hb4", "danger"),
            _button(_["H_B_5"], "help_callback hb5", "primary"),
            _button(_["H_B_6"], "help_callback hb6", "success"),
        ],
        [
            _button(_["H_B_7"], "help_callback hb7", "success"),
            _button(_["H_B_8"], "help_callback hb8", "danger"),
            _button(_["H_B_9"], "help_callback hb9", "primary"),
        ],
        [
            _button(_["H_B_10"], "help_callback hb10", "primary"),
            _button(_["H_B_11"], "help_callback hb11", "success"),
            _button(_["H_B_12"], "help_callback hb12", "danger"),
        ],
        [
            _button(_["H_B_13"], "help_callback hb13", "danger"),
            _button(_["H_B_14"], "help_callback hb14", "primary"),
            _button(_["H_B_15"], "help_callback hb15", "success"),
        ],
    ]

    if START:
        rows.append([
            _button(_["BACK_PAGE"], "mbot_cb", "primary"),
            _button(_["BACK_BUTTON"], "settings_back_helper", "success"),
            _button(_["NEXT_PAGE"], "mbot_cb", "primary"),
        ])
    else:
        rows.append([_button(_["CLOSE_BUTTON"], "close", "danger")])

    return rows


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=f"🔙 {_[ 'BACK_BUTTON' ]}", callback_data="settings_back_helper")]]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=f"❔ {_[ 'S_B_4' ]}",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
