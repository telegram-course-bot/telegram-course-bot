from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="📋 Получить чеклист",
            url="https://t.me/irina_s_vetriny/228?comment=1724"
        ),
        InlineKeyboardButton(
            text="🎥 Смотреть демо-урок",
            url="https://t.me/irina_s_vetriny/229"  # Заменить на актуальную ссылку
        ),
        InlineKeyboardButton(
            text="📦 Программа курса",
            url="https://t.me/irina_s_vetriny/230"  # Заменить на актуальную ссылку
        ),
        InlineKeyboardButton(
            text="💰 Купить курс через Boosty",
            url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"
        ),
        InlineKeyboardButton(
            text="❓ Задать вопрос",
            url="https://t.me/irina_s_vetriny"
        )
    )

    await message.answer(
        "Привет! 🎓 Добро пожаловать! Вот что тебе пригодится:",
        reply_markup=keyboard
    )

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
