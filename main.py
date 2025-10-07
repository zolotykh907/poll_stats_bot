import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.handlers import start_and_help, training_poll
from bot.middleware.poll_manager_middleware import PollManagerMiddleware
from bot.poll_manager import PollManager


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
poll_manager = PollManager(bot)

dp.update.middleware(PollManagerMiddleware(poll_manager))

async def main():
    dp.include_router(start_and_help.router)
    dp.include_router(training_poll.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Бот работает!')
    asyncio.run(main())