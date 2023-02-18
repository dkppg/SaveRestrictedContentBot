#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","14604313", cast=int)
API_HASH = config("API_HASH", "a8ee65e5057b3f05cf9f28b71667203a")
BOT_TOKEN = config("BOT_TOKEN", "6171100757:AAHI5T-DP8wsAX91uhgBc3eMdFpQB4jp2TA")
SESSION = config("SESSION", "BQCx1EliJ7VXcPKYsNOczxdKCv61E0azF94SzVtHfjrdp2WL_RkXZiD2iRl9ebaKDFZMEdQI6bnnKIIuarmBspxh8_pNaF5INZIQiDgSBgWSwSd5XZ4vpxPetusHeFFLWvgb7CaqcAQ-iEVy_Y_D2tcKiNeE1ztw-E9ENrzxl0Xfskx9_MVS7qzSRraGUetCCUMG7UtMxXSf41-NATKsbJyOwFeyoi1GQRtu0OWkP6kzsKHZoliQQd66i56T9g2r69IR50qYXQA8yKLb_SiDP8LZW452Jt0S6SPQq3oYHkSqRSdyLgvGf6pJRcKqUa_1bcZBrPrFm-g6KdwuryY2ozZpAAAAATC3sOgA")
FORCESUB = config("FORCESUB", "saverestrict")
AUTH = config("AUTH", "5112312040", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
