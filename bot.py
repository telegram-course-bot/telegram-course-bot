from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    # Inline кнопки
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(
        InlineKeyboardButton("📋 Получить чеклист", url="https://t.me/irina_s_vetriny/228?comment=1724"),
        InlineKeyboardButton("🎥 Смотреть демо-урок", url="https://t.me/irina_s_vetriny/229"),
        InlineKeyboardButton("📦 Программа курса", url="https://t.me/irina_s_vetriny/230"),
        InlineKeyboardButton("💰 Купить курс через Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"),
        InlineKeyboardButton("❓ Задать вопрос", url="https://t.me/irina_s_vetriny"),
        InlineKeyboardButton("💬 Оставить отзыв", url="https://t.me/irina_s_vetriny")
    )

    # Reply кнопки
    reply_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_kb.add(
        KeyboardButton("📋 Получить чеклист"),
        KeyboardButton("💰 Купить через Boosty")
    )

    await message.answer(
        "👋 Привет! Добро пожаловать в *курс уверенного общения с женщинами*!\n\n"
        "Вот что поможет тебе прямо сейчас:",
        parse_mode="Markdown",
        reply_markup=inline_kb
    )
    await message.answer("👇 Или выбери действие ниже:", reply_markup=reply_kb)

# Команда /feedback
@dp.message_handler(commands=["feedback"])
async def feedback_handler(message: types.Message):
    text = message.get_args()
    if not text:
        await message.reply("Пожалуйста, напиши отзыв после команды, например:\n/feedback Спасибо за курс!")
        return

    admin_id = 394515067  # Твой Telegram ID

    feedback_text = (
        f"💬 *Новый отзыв от* [{message.from_user.full_name}](tg://user?id={message.from_user.id}):\n\n"
        f"{text}"
    )

    try:
        await bot.send_message(admin_id, feedback_text, parse_mode="Markdown")
        await message.reply("Спасибо за отзыв! 🙌")
    except Exception as e:
        await message.reply("Не удалось отправить отзыв. Попробуйте позже.")
        print(e)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
