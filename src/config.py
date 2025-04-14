import os

from dotenv import load_dotenv

load_dotenv()

BOT_NAME = os.environ.get("TGBOT_NAME")
BOT_TOKEN = os.environ.get("TGBOT_TOKEN")