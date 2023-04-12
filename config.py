import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "21840776")) #optional
API_HASH = getenv("API_HASH", "a83dc6bea8b64c2191b2fe631f1097a9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1362133845").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5719989001:AAHkb_pp8Phz1Z8BgbZdp5hXUbWP7bfhqH4")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3b9730e0042579e85c243.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/taitangamer/SpamX")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
