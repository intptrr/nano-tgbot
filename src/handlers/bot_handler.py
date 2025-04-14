import logging

from config import BOT_NAME
from telegram import Update
from telegram.ext import (
  Application,
  CommandHandler,
  MessageHandler,
  ContextTypes,
  filters)

logger = logging.getLogger(__name__)

async def start_handler(update: Update) -> None:
  """
  Handle the /start command.
  """
  await update.message.reply_text("Hi! I'm Nano Bot.")

async def mention_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Handle mentions of the bot.
  """
  user_name = update.effective_user.username
  chat = update.effective_chat

  logger.info("%s mentioned the bot in a chat", user_name)

  context.bot_data.setdefault("user_ids", set()).add(chat.id)
  await update.message.reply_text("How can I help you?")

def setup_handlers(app: Application) -> None:
  """
  Setup all the handlers for the application.
  """
  app.add_handler(CommandHandler("start", start_handler))
  app.add_handler(MessageHandler(filters.Mention(BOT_NAME), mention_handler))