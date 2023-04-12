import logging
import os

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from messages import *

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    exit('Specify TELEGRAM_BOT_TOKEN env variable')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = ReplyKeyboardMarkup([['/about', '/help']])
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=GREETING,
        reply_markup=button
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=ABOUT
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=HELP
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    about_handler = CommandHandler('about', about)
    application.add_handler(about_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    application.run_polling()
