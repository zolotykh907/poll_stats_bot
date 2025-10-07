from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class TrainingPollState(StatesGroup):
    question_state = State()

@router.message(Command("training_poll"))
async def cmd_training_poll(message, state):
    await state.set_state(TrainingPollState.question_state)
    await message.answer("✏️ Введите название опроса:")

    # await poll_manager.create_poll(chat_id=message.chat.id, 
    #                                question=question, 
    #                                options=options)
    
@router.message(TrainingPollState.question_state)
async def poll_get_question(message, state, poll_manager):
    question = message.text
    options = ['Да', 'Нет', 'Тренеры']

    await poll_manager.create_poll(chat_id=message.chat.id, 
                                   question=question, 
                                   options=options)
    await state.clear()


@router.poll_answer()
async def training_poll_answer(poll_answer, poll_manager):
    print(f"💾 Ответ получен от {poll_answer.user.full_name}")
    poll_manager.save_poll_answer(poll_answer)