from pyrogram import Client, enums, filters 
from pyrogram.types import Message 
from config import LOG_GROUP
from SpamX.modules.help import add_command_help
log = []


@Client.on_message(filters.command("tagalert on", ".") & filters.me)
async def set_no_log_p_m(client: Client, message: Message):
    if LOG_GROUP != -100:
        if not message.chat.id in log:
            log.append(message.chat.id)
            await message.edit("**ᴛᴀɢ ᴀʟᴇʀᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**")

@Client.on_message(filters.command("tagalert off", ".") & filters.me)
async def set_no_log_p_m(client: Client, message: Message):
        if not message.chat.id in log:
            log.remove(message.chat.id)
            await message.edit("**ᴛᴀɢ ᴀʟᴇʀᴛ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**")

if log:
 @Client.on_message(filters.group & filters.mentioned & filters.incoming)
 async def log_tagged_messages(client: Client, message: Message):
    result = f"<b>📨 #ᴛᴀɢs #ᴍᴇssᴀɢᴇ</b>\n<b> • : </b>{message.from_user.mention}"
    result += f"\n<b> • ɢʀᴏᴜᴘ : </b>{message.chat.title}"
    result += f"\n<b> • 👀 </b><a href = '{message.link}'>Lihat Pesan</a>"
    result += f"\n<b> • ᴍᴇssᴀɢᴇ : </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        LOG_GROUP,
        result,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )


add_command_help(
    "tagalert",
    [
        [
            "tagalert on/off",
            "To activate or deactivate the group tag, which will go to the log group.",
        ],
    ],
)
