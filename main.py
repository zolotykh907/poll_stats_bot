import asyncio
import os

from aiogram import Bot, Dispatcher
from bot.handlers import start_and_help
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start_and_help.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Бот работает!')
    asyncio.run(main())