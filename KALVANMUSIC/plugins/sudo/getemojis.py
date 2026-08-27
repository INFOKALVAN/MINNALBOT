from pyrogram import filters
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message

from TPMusic import app
from TPMusic.misc import SUDOERS


@app.on_message(filters.command("getemojis") & SUDOERS)
async def get_emoji_ids(client, message: Message):
    target = message.reply_to_message
    if not target:
        return await message.reply_text(
            "**Usage:**\n"
            "Reply to a message that contains the custom/premium emojis "
            "(paste all of them from the pack into one message and send it, "
            "then reply to that message with /getemojis)."
        )

    entities = (target.entities or []) + (target.caption_entities or [])
    text = target.text or target.caption or ""

    found = []
    for ent in entities:
        if ent.type == MessageEntityType.CUSTOM_EMOJI:
            char = text[ent.offset: ent.offset + ent.length]
            found.append((char, ent.custom_emoji_id))

    if not found:
        return await message.reply_text(
            "**No custom/premium emojis found in that message.**\n\n"
            "Note: if you sent the emojis yourself and you don't have Telegram "
            "Premium, Telegram silently downgrades them to regular emojis before "
            "they even reach the bot — in that case forward a message that "
            "*already contains* the custom emojis (e.g. from the pack's preview "
            "chat) instead of typing them fresh."
        )

    lines = [f"**✅ Found {len(found)} custom emoji(s):**\n"]
    for char, emoji_id in found:
        lines.append(f"{char}  →  `{emoji_id}`")

    out = "\n".join(lines)
    if len(out) > 4000:
        chunks = [out[i:i + 4000] for i in range(0, len(out), 4000)]
        for chunk in chunks:
            await message.reply_text(chunk)
    else:
        await message.reply_text(out)
