# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from telethon import Button
from telethon.tl.types import InputWebDocument as wb

from . import *

SUP_BUTTONS = [
    [
        Button.url("• Repo •", url="https://github.com/antoo69/Fs-Userbot"),
        Button.url("• Support •", url="t.me/BestieVirtual"),
    ],
]

ofox = "https://graph.org/file/231f0049fcd722824f13b.jpg"
gugirl = "https://graph.org/file/0df54ae4541abca96aa11.jpg"
aypic = "https://graph.org/file/b0ede17600df06f798774.jpg"

apis = [
    "QUl6YVN5QXlEQnNZM1dSdEI1WVBDNmFCX3c4SkF5NlpkWE5jNkZV",
    "QUl6YVN5QkYwenhMbFlsUE1wOXh3TVFxVktDUVJxOERnZHJMWHNn",
    "QUl6YVN5RGRPS253blB3VklRX2xiSDVzWUU0Rm9YakFLSVFWMERR",
]


@in_pattern("repo", owner=True)
async def repo(e):
    res = [
        await e.builder.article(
            title="𝑭𝒆𝒓𝒅𝒊 𝑼𝒔𝒆𝒓𝒃𝒐𝒕",
            description="𝑼𝒔𝒆𝒓𝒃𝒐𝒕 | Telethon",
            thumb=wb(aypic, 0, "image/jpeg", []),
            text="**◈ 𝑭𝒆𝒓𝒅𝒊 𝑼𝒔𝒆𝒓𝒃𝒐𝒕 ◈**",
            buttons=SUP_BUTTONS,
        ),
    ]
    await e.answer(res, switch_pm="𝑭𝒆𝒓𝒅𝒊 𝑼𝒔𝒆𝒓𝒃𝒐𝒕", switch_pm_param="start")
