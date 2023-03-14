import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "SpamX"])

async def join(client):
    try:
        await client.join_chat("Its_Venom_family")
    except BaseException:
        pass
