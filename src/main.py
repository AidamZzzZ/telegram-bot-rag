import os
import asyncio
import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

async def main():
    bot = telegram.Bot(TELEGRAM_API_KEY)
    async with bot:
        await bot.send_message(text='Hi John!', chat_id=1234567890)

if __name__ == '__main__':
    asyncio.run(main())