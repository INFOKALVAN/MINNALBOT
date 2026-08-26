from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from config import *
from KALVANMUSIC import app
from KALVANMUSIC.core.call import KALVAN
from KALVANMUSIC.utils import bot_sys_stats
from KALVANMUSIC.utils.decorators.language import language
from KALVANMUSIC.utils.colored_buttons import buttons_to_inline_markup
from KALVANMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_VID_URL


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video=PING_VID_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await KALVAN.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        text=_["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=buttons_to_inline_markup(supp_markup(_)),
    )
