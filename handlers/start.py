import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkDAAKA82P--qL066ND9OgiRoasosU3hmCnAAJVAQACB-QBVGNqeJnsWN7QHgQ")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , ⚔️\n\n
๏ This is [{bn}](t.me/{bu})
➻ 👑Official Account ✅
⚡My Life My Rules💪
🎶Music ka Diwana💥
🕉️Mahadev Bhakt🕉️
♍I’m not Rich ßut I’m Royal 👑
🌹Loyal and trustable Boy👩‍❤️‍👨
☺️My Freinds are my World 💗.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🫶🏻 by : [𝙆𝙍𝙄𝙎𝙃𝙉𝘼❤️‍🔥](https://t.me/krishna_op_143) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚Add Me To Your Group✚  ", url=f"https://t.me/CRUSH_MUSIC_ASSISTANCE_BOT?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "⚔️ Support My Channel  ", url=f"https://t.me/CRUSH_WORLD_DP_GIF_ZONE"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Support My Group ", url=f"https://t.me/TOXIC_WORLD_2"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Real Owner ", url=f"https://t.me/krishna_op_143"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/krishna_op_143"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4"
                    )]
            ]
       ),
    )

