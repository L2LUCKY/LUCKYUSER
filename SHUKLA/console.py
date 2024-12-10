import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "25609334"))
API_HASH = getenv("API_HASH", "ad0ff353206ea1ebce1ab8bfca9f3f7b")
BOT_TOKEN = getenv("BOT_TOKEN", "7209856039:AAFH5FrVO5vDAFVXqeQ9RgcMFfmSyH4z5po")
STRING_SESSION = getenv("STRING_SESSION", "BQCl648AQTBBQISdKMBzpUxXggc6Zw9HutRxh0MdN2qsE3SYls5LF-rkI8zBmFlurbW5rqT-O_nfr53NNqe_Luq1TJIJPHOoDDYGcliAK4swKAfZ_qQbX787dRV3lY7qmqSwurdXkyjfVkgA6MsHnobkNpbotajL4uL0T2dfOE9j9sokldeRl34kTM_iU2R1cuR1xqtLUhmOQ8TiPR71C1nxvnl3m2nJxE3GX_1XUZqIZ4teBVPEQmbewvpW0yfY8VbZ1Ij2XOIAm4af2NPa3tNd1oBtAzVm4P09I3arrTOEdoT5P6Fs73ym5Yu46oeM-tQZVMzUE-LTXvOzeA8PQ3HNqmNbMgAAAAGSUQ9QAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Lucky:Lucky@atlascluster.f7lck9c.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002021288289"))
OWNER_ID = int(getenv("OWNER_ID", "5247304559"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "itz_Lucky_Raja")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6615076069").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", False))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ꜱᴜᴘᴇʀꜰᴀꜱᴛ ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴜꜱᴇʀʙᴏᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴡɪᴛʜ ᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴠᴇʀꜱɪᴏɴ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ.\n\n🌿 ɪ ᴄᴀɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇꜱꜱᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴅᴍ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ.\n\n❤️ ᴍʏ ᴏᴡɴᴇʀ ɪꜱ ᴏꜰꜰʟɪɴᴇ ɴᴏᴡ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ᴏᴡɴᴇʀ ᴀʟʟᴏᴡꜱ ʏᴏᴜ.\n\n🍂 ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ, ʙᴇᴄᴀᴜꜱᴇ ꜱᴘᴀᴍᴍɪɴɢ ᴡɪʟʟ ꜰᴏʀᴄᴇ ᴍᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ ɪᴅ 👍🏻**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

