from aiogram import types, Router
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Я бот для опросов.\nИспользуй /help, чтобы узнать команды.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("📖 Доступные команды:\n/start — приветствие\n/help — помощь")