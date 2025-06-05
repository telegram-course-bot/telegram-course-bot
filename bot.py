from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
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

# Состояния теста
class TestStates(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()

# Главное маркетинговое меню
def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📋 Получить чеклист", "🎥 Смотреть демо-урок")
    keyboard.add("📦 Программа курса", "🔥 Купить курс через Boosty")
    keyboard.add("🧠 Пройти мини-тест", "❓ Задать вопрос")
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu())

# Реакции на кнопки основного меню
@dp.message_handler(lambda m: m.text == "📋 Получить чеклист")
async def checklist(message: types.Message):
    await message.answer("Вот твой чеклист ✅:
1. Подумай о целях...
2. ...")

@dp.message_handler(lambda m: m.text == "🎥 Смотреть демо-урок")
async def demo_lesson(message: types.Message):
    await message.answer("🎬 Демо-урок: https://t.me/your_demo_lesson")

@dp.message_handler(lambda m: m.text == "📦 Программа курса")
async def course_outline(message: types.Message):
    await message.answer("📚 Программа курса:
- Урок 1
- Урок 2
...")

@dp.message_handler(lambda m: m.text == "🔥 Купить курс через Boosty")
async def buy_course(message: types.Message):
    await message.answer("🚀 Купить курс: https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link")

@dp.message_handler(lambda m: m.text == "❓ Задать вопрос")
async def ask_question(message: types.Message):
    await message.answer("Напиши свой вопрос, и я передам его автору курса.")

# Тест — запуск из меню
@dp.message_handler(lambda m: m.text == "🧠 Пройти мини-тест")
async def start_test(message: types.Message, state: FSMContext):
    await message.answer("🧠 Вопрос 1: Ты легко выражаешь свои чувства?")
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
