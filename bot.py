from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("📋 Получить чеклист", url="https://t.me/irina_s_vetriny/228?comment=1724"),
        types.InlineKeyboardButton("🎥 Смотреть демо-урок", callback_data="demo"),
        types.InlineKeyboardButton("📦 Программа курса", callback_data="program"),
        types.InlineKeyboardButton("🔥 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
        types.InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/Grenka_IR")
    )
    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\nВот что поможет тебе прямо сейчас:",
        reply_markup=keyboard
    )

@dp.callback_query_handler(lambda c: True)
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer()
    if callback.data == "demo":
        await callback.message.answer("🎥 Демо-урок появится скоро.")
    elif callback.data == "program":
        await callback.message.answer("📦 Программа курса:\n1. Введение\n2. Уверенность\n3. Общение\n4. Практика")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
