from aiogram import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("training_poll"))
async def cmd_training_poll(message, state, poll_manager):
    question = 'Тренировка завтра'
    options = ['Да', 'Нет', 'Тренеры']

    await poll_manager.create_poll(chat_id=message.chat.id, 
                                   question=question, 
                                   options=options)
