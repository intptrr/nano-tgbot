import os

from dotenv import load_dotenv

load_dotenv()

BOT_NAME = os.getenv("TGBOT_NAME")
BOT_TOKEN = os.getenv("TGBOT_TOKEN")