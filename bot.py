from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="📋 Получить чеклист",
            url="https://t.me/irina_s_vetriny/228?comment=1724"
        ),
        InlineKeyboardButton(
            text="💰 Купить курс через Boosty",
            url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"
        )
    )

    await message.answer(
        "Привет! 🎓 Добро пожаловать! Вот что тебе пригодится:",
        reply_markup=keyboard
    )
