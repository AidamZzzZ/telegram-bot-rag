import os
import asyncio
import telegram
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

load_dotenv()

# telegram API key
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

async def main():
    bot = telegram.Bot(TELEGRAM_API_KEY)
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=-123123123)

# comando /start
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='I\'m a bot, please talk to me!')

if __name__ == '__main__':
    # construtor de aplicacion con token
    application = Application.builder().token(TELEGRAM_API_KEY).build()
    # manejador
    application.add_handler(CommandHandler("start", start))
    # ejecucion del bot
    print("Bot ejecutandose...")
    application.run_polling()
    