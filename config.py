from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21568806"))
API_HASH = getenv("API_HASH", "83c41043d5ada58ad3dc95652afa70d5")

BOT_TOKEN = getenv("BOT_TOKEN", "6819381670:AAGHM2b7aJHP_GE0LnXI8elW9odocGopieA")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://avineyjr004:Sindhu@003@cluster0.cqunmib.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", "1556830659"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/we_are_universee")
