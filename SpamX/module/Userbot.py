# Venom - Telegram Projects
# (c) 2022 - 2023 Venom
# Don't Kang Bitch -!


import os
import sys
import asyncio
import datetime
import time
from SpamX import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "ᴠᴇɴᴏᴍ X sᴘᴀᴍ"
VENOM_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/f312793bf706724dbeca2.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝗩𝗲𝗻𝗼𝗺 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲."


venom = f"⁂ {Alivemsg} ⁂\n\n"
venom += f"━───────╯•╰───────━\n"
venom += f"➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.4`\n"
venom += f"➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{pyro_vr}`\n"
venom += f"➠ **SᴘᴀᴍX ᴠᴇʀsɪᴏɴ**  : `{__version__}`\n"
venom += f"➠ **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/Its_Venom_family)\n"
venom += f"━───────╮•╭───────━\n\n"
venom += f"➠ **Source Code:** [•Repo•](https://github.com/Itzvenomo/SpamX)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["alive"], prefixes=HNDLR))
async def alive(xspam: Client, e: Message):
       if ".jpg" in VENOM_PIC or ".png" in VENOM_PIC:
              await xspam.send_photo(e.chat.id, VENOM_PIC, caption=venom)
       if ".mp4" in VENOM_PIC or ".MP4," in VENOM_PIC:
              await xspam.send_video(e.chat.id, VENOM_PIC, caption=venom)



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=HNDLR))
async def reboot(xspam: Client, e: Message):
        reboot_text = "**Re-starting** \n\n __Wait For A While To Use it Again__ "
        await e.reply_text(reboot_text)
        try:
            xspam.disconnect()
        except Exception as e:
            pass
        args = [sys.executable, "-m", "SpamX"]
        os.execl(sys.executable, *args)
        quit()

            
