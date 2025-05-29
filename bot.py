from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
import logging
import os

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
menu = InlineKeyboardMarkup(row_width=1)
menu.add(
    InlineKeyboardButton("📄 Получить чеклист", callback_data="get_checklist"),
    InlineKeyboardButton("🎥 Смотреть демо-урок", url="https://t.me/irina_s_vetriny/229"),
    InlineKeyboardButton("📦 Программа курса", url="https://t.me/irina_s_vetriny/230"),
    InlineKeyboardButton("💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
    InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/irina_s_vetriny"),
    InlineKeyboardButton("💬 Оставить отзыв", url="https://t.me/irina_s_vetriny")
)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    logging.info(f"User {message.from_user.id} started the bot.")
    await message.answer(
        "👋 Привет! Добро пожаловать в курс уверенного общения с женщинами!\n\nВот что поможет тебе прямо сейчас:",
        reply_markup=menu
    )

@dp.callback_query_handler(lambda c: c.data == "get_checklist")
async def send_checklist(callback_query: types.CallbackQuery):
    logging.info(f"User {callback_query.from_user.id} requested checklist.")
    try:
        with open("checklist.pdf", "rb") as doc:
            await bot.send_document(callback_query.from_user.id, doc)
        await bot.answer_callback_query(callback_query.id)
    except Exception as e:
        logging.error(f"Ошибка при отправке файла: {e}")
        await bot.send_message(callback_query.from_user.id, "🚫 Ошибка: файл не найден.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
