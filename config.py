import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID & API HASH from my.telegram.org
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001971345822"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2048030675"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filestore34")

#Shortner (token system) 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "tnshort.net/")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "28b13d9bb65763440a73ae4a280d4e1be4cc4ef1")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/mr_v_bots/1890") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001657088649"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ🖐 {first}\n\nI ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ғɪʟᴇs ғʀᴏᴍ <a href='https://t.me/A1pher'>Tᗴᗩᗰ ᗩ1ᑭᕼᗴᖇ</a> ᴛᴏ ᴍʏ ғᴀᴍɪʟʏ ᴀɴᴅ ᴛʜᴇʏ ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ᴡɪᴛʜ ᴍʏ ʟɪɴᴋs.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2048030675").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ🖐 {first}\n\n<b>Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ's ᴛᴏ ᴜsᴇ ᴍᴇ\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ Cʜᴀɴɴᴇʟ</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Mʏ ᴀʙɪʟɪᴛʏ ɪs ᴛᴏ sᴇɴᴅ ғɪʟᴇs ᴏɴʟʏ"

ADMINS.append(OWNER_ID)
ADMINS.append(2048030675)

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
