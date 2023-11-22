from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ???