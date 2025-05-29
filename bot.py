import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Включение логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Удаление вебхука перед запуском бота
async def on_startup(dp):
    await bot.delete_webhook(drop_pending_updates=True)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📄 Получить чеклист", url="https://t.me/irina_s_vetriny/228"),
        InlineKeyboardButton("🎥 Смотреть демо-урок", callback_data="demo"),
        InlineKeyboardButton("📦 Программа курса", callback_data="program"),
        InlineKeyboardButton("💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
        InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/Grenka_IR")
    )

    text = (
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\n"
        "Вот что поможет тебе прямо сейчас:"
    )
    await message.answer(text, reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
