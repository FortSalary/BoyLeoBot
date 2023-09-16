from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/21c4b1f265402c80ebe1f.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BoyLeo_Support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BoyyLeoo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5075416614").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
