from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Бот работает 🔥")

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
