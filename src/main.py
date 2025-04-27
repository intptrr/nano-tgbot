import handlers
import logging

from config import BOT_TOKEN
from telegram import Update
from telegram.ext import Application

logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():  
  app = Application.builder().token(BOT_TOKEN).build()
  logger.info("Bot started")

  handlers.setup_handlers(app)

  app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
  main()