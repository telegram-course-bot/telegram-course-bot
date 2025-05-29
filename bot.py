import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Загрузка токена из .env файла
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("📄 Получить чеклист", url="https://t.me/irina_s_vetriny/228?comment=1724"),
        types.InlineKeyboardButton("🎓 Смотреть демо-урок", url="https://t.me/irina_s_vetriny"),
        types.InlineKeyboardButton("📦 Программа курса", url="https://t.me/irina_s_vetriny"),
        types.InlineKeyboardButton("💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
        types.InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/Grenka_IR")
    ]
    keyboard.add(*buttons)
    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\n"
        "Вот что поможет тебе прямо сейчас:",
        reply_markup=keyboard
    )

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
