import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram import F
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="📋 Получить чеклист", url="https://t.me/irina_s_vetriny/228"))
    kb.row(InlineKeyboardButton(text="🎓 Смотреть демо-урок", url="https://example.com/demo"))
    kb.row(InlineKeyboardButton(text="📦 Программа курса", url="https://example.com/program"))
    kb.row(InlineKeyboardButton(text="💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"))
    kb.row(InlineKeyboardButton(text="❓ Задать вопрос", url="https://t.me/Grenka_IR"))
    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\nВот что поможет тебе прямо сейчас:",
        reply_markup=kb.as_markup()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
