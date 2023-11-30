import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config

import weather

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Let's get you some weather info"
    )

async def temperature(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #current_temperature = weather.get_temperature()
    await update.message.reply_text(weather.get_temperature())

if __name__ == '__main__':
    application = ApplicationBuilder().token(str(config.api_key)).build()

    start_handler = CommandHandler('start', start)
    temperature_handler = CommandHandler('temperature', temperature)

    application.add_handler(start_handler)
    application.add_handler(temperature_handler)

    application.run_polling()