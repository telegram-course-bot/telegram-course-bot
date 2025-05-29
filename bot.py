
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

API_TOKEN = '7985180070:AAHn98xLc8H_JPVtzrYftMiZu0lbeEQwf6M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Основное меню
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="📋 Получить чеклист")],
    [KeyboardButton(text="💰 Купить через Boosty")]
])

# Кнопка Boosty
boosty_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💰 Перейти на Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b")]
])

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Это бот курса 'Не теряй себя'.\n\nВыбери, что тебе нужно:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "📋 Получить чеклист")
async def send_checklist(message: types.Message):
    await message.answer_document(types.FSInputFile("Чеклист_и_шпаргалка.pdf"))

@dp.message(lambda message: message.text == "💰 Купить через Boosty")
async def send_boosty(message: types.Message):
    await message.answer(
        "👉 Оплати курс по кнопке ниже. Если не открывается — нажми ⋮ вверху и выбери «Открыть в браузере».",
        reply_markup=boosty_button
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
