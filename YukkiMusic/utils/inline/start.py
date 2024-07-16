#
# Copyright (C) 2024-2025 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the MIT License.
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
            ),
        ], 
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
        ),
        ],
      [
            InlineKeyboardButton(
               text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", 
               user_id=OWNER,
                    ),
           InlineKeyboardButton(
               text="sᴜᴘᴘᴏʀᴛ",
               url=f"https://t.me/CODERZCHAT"
           ),
        ],
      [
            InlineKeyboardButton(
               text="Lᴀɴɢᴜᴀɢᴇ", 
               callback_data="LG"
                    ),
           InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ",
                callback_data="source_codeprank"
                   ),
        ],
]
    return buttons
