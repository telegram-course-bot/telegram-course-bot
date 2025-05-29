from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "📄 Получить чеклист",
        "💰 Купить через Boosty"
    ]
    keyboard.add(*buttons)

    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\n"
        "Вот что поможет тебе прямо сейчас:",
        reply_markup=keyboard
    )

# Обработка кнопки "Получить чеклист"
@dp.message_handler(lambda message: message.text == "📄 Получить чеклист")
async def send_checklist(message: types.Message):
    with open("course.pdf", "rb") as pdf:
        await message.answer_document(pdf, caption="Вот твой чеклист 💼")

# Обработка кнопки "Купить через Boosty"
@dp.message_handler(lambda message: message.text == "💰 Купить через Boosty")
async def send_boosty_link(message: types.Message):
    await message.answer("Оплата и доступ к курсу: https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link")

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
