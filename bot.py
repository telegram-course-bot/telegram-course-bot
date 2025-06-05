from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

# Главное меню
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🧠 Пройти тест на отношения", callback_data="start_test"),
        InlineKeyboardButton("🎥 Смотреть демо-видео", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        InlineKeyboardButton("🚀 Купить курс на Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link")
    )
    await message.answer("👋 Привет! Это бот по отношениям. Выбери, что тебе интересно:", reply_markup=keyboard)

# Обработка кнопки теста
@dp.callback_query_handler(lambda c: c.data == "start_test")
async def start_test(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🧠 Начнём тест: Насколько ты уверена в себе в отношениях?\nОтветь: да или нет.

1. Часто ли ты сомневаешься в своих действиях?
Ответь: да или нет.

# Ответ на текст
@dp.message_handler(lambda message: message.text.lower() in ["да", "нет"])
async def test_continue(message: types.Message):
    if message.text.lower() == "да":
        await message.answer("❗ Это сигнал: тебе важно разобраться в себе. Курс может сильно помочь тебе! 💬")
    else:
        await message.answer("💡 Отлично! Но возможно, ты найдёшь в курсе ещё больше полезного.")
    await message.answer("👉 [Нажми здесь, чтобы перейти к курсу](https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link)", parse_mode="Markdown")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
