from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Кнопки меню
menu_keyboard = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("📋 Получить чеклист", url="https://t.me/irina_s_vetriny/228"),
    InlineKeyboardButton("📹 Смотреть демо-урок", callback_data="demo"),
    InlineKeyboardButton("📦 Программа курса", callback_data="program"),
    InlineKeyboardButton("💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
    InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/Grenka_IR")
)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\n"
        "Вот что поможет тебе прямо сейчас:",
        reply_markup=menu_keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
