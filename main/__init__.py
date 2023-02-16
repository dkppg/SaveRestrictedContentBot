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
SESSION = config("SESSION", "BQBTox4VZ4_aGl9bqcSo3uRsYmW6rKGNLSR0ayZPx5-bp6qPVAxA5ygBLZ4Tc_DNZCxPSVlBZGxABN0qVt0IsgUMm93V0HtzugO05owFr1TxcxO1Rb49O194QF46MYh2JRJxFzJuKVrJjoulavUD7C2uCohPeow5ac1dY7Z2f6YLw_tmf-ZSmKb8h0cJf1MJiNWRX4khLz--S8hQDzg0bZwgztLQp_9_12dVsjmBi-j-7MFJ99UhRWlKxeR7OhP3VKPjvbR6MzWlbR-26YcubRh2kOZ03HQ8yTNEUH7fBnn5Zb-pj-vlWAT23A3sHP5VGHSVkIiCn6IeDzJOEBCBgQuIAAAAATC3sOgA")
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
