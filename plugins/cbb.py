#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Master : <a href='https://t.me/COLD_ONEz'>COLD_ONEz</a>\n\n○ Master : <a href='https://t.me/mrk_yt'>MRK_YT</a>\n\n○ Group : <a href='https://t.me/Mo_Tech_Group'>Mo_Tech_Group</a>\n\n○ Channel : <a href='https://t.me/Mo_Tech_YT'>Mo_Tech_YT</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
