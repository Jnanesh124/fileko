#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6907169649:AAHwIcBR8bNR5Lk5TvtuDa3UphBvJKxzKRk")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19937650"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a6df8006df3cb56edce33056d37baca")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001953742196"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6605647659"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jnanesh:jnanesh@cluster0.8pzxa6s.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filestorenk")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002012970688"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "MovieRequestGroup :- https://t.me/+5TJUbOMCqD05ZmQ1 onlineStreamingmovies:- https://t.me/+oQT1f1iF4fU4ZGVl OTT released Movies :- https://t.me/+D7L-rX9lKA43MGRl Adult Video :- https://t.me/+Ce98xoyvoLcwYThl")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6605647659").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel To Get File\n\nand subscribe my YouTube Channel :- https://youtube.com/@Jnentertainment.?si=-xZOdUGBD3yxLjgW</b>")

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
USER_REPLY_TEXT = "🍿Request Your movies here  https://t.me/+5TJUbOMCqD05ZmQ1" 

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
