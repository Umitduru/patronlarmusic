from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("")
BOT_NAME = getenv("BOT_NAME", "BusraMuzikBot") 
API_ID = int(getenv("API_ID")19757862)
API_HASH = getenv("7131164622:AAGLsJLFilmVEGfslTMoNIHAErIQPryjJow")
BOT_USERNAME = getenv("BOT_USERNAME", "BusraMuzik_bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split(6790545367)))
