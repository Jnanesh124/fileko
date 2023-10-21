#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5658733188:AAHTV-2dHHoBD-_CirA22nsXngmlydvMXWM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13271631"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c53ac45c5e24205743c58ed8a748b90a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001886911325"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5047601096"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filestorenk")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001654950491"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝑯𝒆𝒚 {first} 𝑰 𝒂𝒎 𝒇𝒊𝒍𝒆 𝒔𝒕𝒐𝒓𝒆 𝒃𝒐𝒕 𝒏𝒐𝒕 𝒂𝒏𝒐𝒕𝒉𝒆𝒓 𝒃𝒐𝒕 𝑰 𝒄𝒂𝒏 𝒔𝒕𝒐𝒓𝒆 𝒖𝒓 𝒇𝒊𝒍𝒆 𝒂𝒏𝒅 𝑰 𝒘𝒊𝒍𝒍 𝒈𝒊𝒗𝒆 𝒚𝒐𝒖 𝒔𝒉𝒂𝒓𝒆𝒂𝒃𝒍𝒆 𝒍𝒊𝒏𝒌 𝒖 𝒄𝒂𝒏 𝒖𝒔𝒆 𝒕𝒉𝒂𝒕 𝒍𝒊𝒏𝒌 𝒕𝒐 𝒈𝒆𝒕 𝒖𝒓 𝒇𝒊𝒍𝒆𝒔 𝒂𝒏𝒚 𝒕𝒊𝒎𝒆 𝒖 𝒂𝒍𝒔𝒐 𝒔𝒉𝒂𝒓𝒕 𝒕𝒉𝒂𝒕 𝒍𝒊𝒏𝒌")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1384893863").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🛎Request Your movies here  https://t.me/+Pg5xeggLye5lZDA1 
                   🚦OTT Movies HD https://t.me/+D7L-rX9lKA43MGRl"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
