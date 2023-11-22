import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Let's get you some weather info"
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(str(config.api_key)).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()