from dotenv import load_dotenv
import os


load_dotenv()

# api Configuration
API_ID = int(os.getenv("API_ID", "10248430"))  
API_HASH = os.getenv("API_HASH", "42396a6ff14a569b9d59931643897d0d")  
# @var
#Please generate a session using @elite_session_maker_bot else your session not working 
ELITE_SESSION = os.getenv("ELITE_SESSION", "1BVtsOIEBuzqwUdBZAg0Y3sYU4396JsEhy63jcn3DJtbzC5kDHRLMn-u52bGLD_ZD0Vq7iqfmiRYBQJ9Ahq2k6T8FmWIA2Bmdw9hN4nK8QpYMPCHECyX73GOHmpY9Jzqedc3zlPcjINnyx78XLf6Wvnhva5vQ6duXcrWYVKLp2ZZeHXLnqBv2Sf9GstAnTdqGaIx0ZxR2fFPrUb57sMsqZwI5f9CmQFST9D89UW3J3Y7CBn8bCwB5nJT-7vnpTYk0ohP80c_qneIyd17p-ckULMoO2SNHMiG1LhJFh_juGIlwgXZ5XFJlAfWsSQtEI7fpbs_gkXULpnkqPT1Zwn5PqdFqb5sqA8DEqiQLDWvXx9oqRLXlmbgGCHB4=")  
# Bot Settings
ELITE_BOT_PREFIX = os.getenv("ELITE_BOT_PREFIX", ".")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8683659714:AAHqFgP2vwB0jqLZ_O4udSsC6xmqZm_MVY0")
ELITE_BOT_USERNAME = os.getenv("ELITE_BOT_USERNAME", "@Kaamchoribobot")

# Access Control
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "6704504868").split(",") if x.strip()]
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID", "-1003987520286"))

# Image URLs
PMPERMIT_PIC = os.getenv("PMPERMIT_PIC", "https://ibb.co/nNYNZpNy")  
ALIVE_PIC = os.getenv("ALIVE_PIC", "https://ibb.co/nNYNZpNy") 
PING_PIC = os.getenv("PING_PIC", "https://ibb.co/nNYNZpNy")

# alive name
ALIVE_NAME = os.getenv("ALIVE_NAME", "🪶‌‌‌‌का‌म‌चो‌ऱ ‌हूँ‌༎")  

# Update Configuration
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/rishabhops/CipherElite")
BRANCH = os.getenv("BRANCH", "🪶‌‌‌‌का‌म‌चो‌ऱ ‌हूँ‌༎")

# for  debugging dont edit this
if API_ID == 0:
    print("Warning: API_ID is not set. Please update .env with a valid API_ID.")
if API_HASH == "INVALID_API_HASH":
    print("Warning: API_HASH is not set. Please update .env with a valid API_HASH.")
if ELITE_SESSION == "INVALID_SESSION":
    print("Warning: ELITE_SESSION is not set. Please generate a session using @elite_session_maker_bot.")
if BOT_TOKEN == "INVALID_BOT_TOKEN":
    print("Warning: BOT_TOKEN is not set. Please update .env with a valid bot token from @BotFather.")
if ELITE_BOT_USERNAME == "@InvalidBotUsername":
    print("Warning: ELITE_BOT_USERNAME is not set. Please update .env with your bot username.")
if SUDO_USERS == [0]:
    print("Warning: SUDO_USERS is not set. Please update .env with valid Telegram user ID(s).")
if LOG_CHAT_ID == 0:
    print("Warning: LOG_CHAT_ID is not set. Please update .env with a valid logger group ID.")
