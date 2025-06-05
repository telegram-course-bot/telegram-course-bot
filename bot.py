from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Курсы
course = [
    "Урок 1: Введение в отношения.",
    "Урок 2: Эффективное общение.",
    "Урок 3: Решение конфликтов.",
    "Урок 4: Поддержание доверия.",
    "Урок 5: Завершение курса."
]

# Состояния курса
class CourseStates(StatesGroup):
    lesson = State()

# Состояния теста
class TestStates(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()

# Главное меню
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📘 Начать курс", callback_data='start_course'))
    keyboard.add(InlineKeyboardButton("🧠 Пройти мини-тест", callback_data='start_test'))
    await message.answer("Привет! Добро пожаловать в курс по отношениям.
Выбери, с чего начнём:", reply_markup=keyboard)

# Курс
@dp.callback_query_handler(lambda c: c.data == 'start_course')
async def start_course(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(lesson_number=0)
    await CourseStates.lesson.set()
    await send_lesson(callback_query.message, state)

@dp.callback_query_handler(lambda c: c.data == 'next_lesson', state=CourseStates.lesson)
async def next_lesson(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lesson_number = data.get('lesson_number', 0) + 1
    if lesson_number < len(course):
        await state.update_data(lesson_number=lesson_number)
        await send_lesson(callback_query.message, state)
    else:
        await callback_query.message.answer("Курс завершен! Спасибо за участие.")
        await state.finish()

async def send_lesson(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lesson_number = data.get('lesson_number', 0)
    lesson = course[lesson_number]
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Далее", callback_data='next_lesson'))
    await message.answer(f"{lesson}", reply_markup=keyboard)

# Тест
@dp.callback_query_handler(lambda c: c.data == 'start_test')
async def start_test(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("🧠 Вопрос 1: Ты легко выражаешь свои чувства?")
    await TestStates.q1.set()

@dp.message_handler(state=TestStates.q1)
async def test_q1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text.lower())
    await message.answer("Вопрос 2: Ты умеешь слушать партнёра?")
    await TestStates.q2.set()

@dp.message_handler(state=TestStates.q2)
async def test_q2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text.lower())
    await message.answer("Вопрос 3: Ты знаешь, как управлять конфликтами?")
    await TestStates.q3.set()

@dp.message_handler(state=TestStates.q3)
async def test_q3(message: types.Message, state: FSMContext):
    await state.update_data(q3=message.text.lower())
    data = await state.get_data()

    score = 0
    if "да" in data["q1"]: score += 1
    if "да" in data["q2"]: score += 1
    if "да" in data["q3"]: score += 1

    if score == 3:
        text = "Ты отлично подготовлен! 🌟 Но всегда есть чему поучиться..."
    elif score == 2:
        text = "Ты на правильном пути. Немного практики — и будет отлично! 👍"
    else:
        text = "Похоже, тебе пригодится поддержка и знания. 👇"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🚀 Перейти к курсу на Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"))
    await message.answer(text, reply_markup=keyboard)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
