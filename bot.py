from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# РЎРѕСЃС‚РѕСЏРЅРёСЏ С‚РµСЃС‚Р°
class TestStates(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()

# Р“Р»Р°РІРЅРѕРµ РјР°СЂРєРµС‚РёРЅРіРѕРІРѕРµ РјРµРЅСЋ
def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("рџ“‹ РџРѕР»СѓС‡РёС‚СЊ С‡РµРєР»РёСЃС‚", "рџЋҐ РЎРјРѕС‚СЂРµС‚СЊ РґРµРјРѕ-СѓСЂРѕРє")
    keyboard.add("рџ“¦ РџСЂРѕРіСЂР°РјРјР° РєСѓСЂСЃР°", "рџ”Ґ РљСѓРїРёС‚СЊ РєСѓСЂСЃ С‡РµСЂРµР· Boosty")
    keyboard.add("рџ§  РџСЂРѕР№С‚Рё РјРёРЅРё-С‚РµСЃС‚", "вќ“ Р—Р°РґР°С‚СЊ РІРѕРїСЂРѕСЃ")
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ! Р’С‹Р±РµСЂРёС‚Рµ РґРµР№СЃС‚РІРёРµ:", reply_markup=main_menu())

# Р РµР°РєС†РёРё РЅР° РєРЅРѕРїРєРё РѕСЃРЅРѕРІРЅРѕРіРѕ РјРµРЅСЋ
@dp.message_handler(lambda m: m.text == "рџ“‹ РџРѕР»СѓС‡РёС‚СЊ С‡РµРєР»РёСЃС‚")
async def checklist(message: types.Message):
    await message.answer("Р’РѕС‚ С‚РІРѕР№ С‡РµРєР»РёСЃС‚ вњ…:
1. РџРѕРґСѓРјР°Р№ Рѕ С†РµР»СЏС…...
2. ...")

@dp.message_handler(lambda m: m.text == "рџЋҐ РЎРјРѕС‚СЂРµС‚СЊ РґРµРјРѕ-СѓСЂРѕРє")
async def demo_lesson(message: types.Message):
    await message.answer("рџЋ¬ Р”РµРјРѕ-СѓСЂРѕРє: https://t.me/your_demo_lesson")

@dp.message_handler(lambda m: m.text == "рџ“¦ РџСЂРѕРіСЂР°РјРјР° РєСѓСЂСЃР°")
async def course_outline(message: types.Message):
    await message.answer("рџ“љ РџСЂРѕРіСЂР°РјРјР° РєСѓСЂСЃР°:
- РЈСЂРѕРє 1
- РЈСЂРѕРє 2
...")

@dp.message_handler(lambda m: m.text == "рџ”Ґ РљСѓРїРёС‚СЊ РєСѓСЂСЃ С‡РµСЂРµР· Boosty")
async def buy_course(message: types.Message):
    await message.answer("рџљЂ РљСѓРїРёС‚СЊ РєСѓСЂСЃ: https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link")

@dp.message_handler(lambda m: m.text == "вќ“ Р—Р°РґР°С‚СЊ РІРѕРїСЂРѕСЃ")
async def ask_question(message: types.Message):
    await message.answer("РќР°РїРёС€Рё СЃРІРѕР№ РІРѕРїСЂРѕСЃ, Рё СЏ РїРµСЂРµРґР°Рј РµРіРѕ Р°РІС‚РѕСЂСѓ РєСѓСЂСЃР°.")

# РўРµСЃС‚ вЂ” Р·Р°РїСѓСЃРє РёР· РјРµРЅСЋ
@dp.message_handler(lambda m: m.text == "рџ§  РџСЂРѕР№С‚Рё РјРёРЅРё-С‚РµСЃС‚")
async def start_test(message: types.Message, state: FSMContext):
    await message.answer("рџ§  Р’РѕРїСЂРѕСЃ 1: РўС‹ Р»РµРіРєРѕ РІС‹СЂР°Р¶Р°РµС€СЊ СЃРІРѕРё С‡СѓРІСЃС‚РІР°?")
    await TestStates.q1.set()

@dp.message_handler(state=TestStates.q1)
async def test_q1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text.lower())
    await message.answer("Р’РѕРїСЂРѕСЃ 2: РўС‹ СѓРјРµРµС€СЊ СЃР»СѓС€Р°С‚СЊ РїР°СЂС‚РЅС‘СЂР°?")
    await TestStates.q2.set()

@dp.message_handler(state=TestStates.q2)
async def test_q2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text.lower())
    await message.answer("Р’РѕРїСЂРѕСЃ 3: РўС‹ Р·РЅР°РµС€СЊ, РєР°Рє СѓРїСЂР°РІР»СЏС‚СЊ РєРѕРЅС„Р»РёРєС‚Р°РјРё?")
    await TestStates.q3.set()

@dp.message_handler(state=TestStates.q3)
async def test_q3(message: types.Message, state: FSMContext):
    await state.update_data(q3=message.text.lower())
    data = await state.get_data()

    score = 0
    if "РґР°" in data["q1"]: score += 1
    if "РґР°" in data["q2"]: score += 1
    if "РґР°" in data["q3"]: score += 1

    if score == 3:
        text = "РўС‹ РѕС‚Р»РёС‡РЅРѕ РїРѕРґРіРѕС‚РѕРІР»РµРЅ! рџЊџ РќРѕ РІСЃРµРіРґР° РµСЃС‚СЊ С‡РµРјСѓ РїРѕСѓС‡РёС‚СЊСЃСЏ..."
    elif score == 2:
        text = "РўС‹ РЅР° РїСЂР°РІРёР»СЊРЅРѕРј РїСѓС‚Рё. РќРµРјРЅРѕРіРѕ РїСЂР°РєС‚РёРєРё вЂ” Рё Р±СѓРґРµС‚ РѕС‚Р»РёС‡РЅРѕ! рџ‘Ќ"
    else:
        text = "РџРѕС…РѕР¶Рµ, С‚РµР±Рµ РїСЂРёРіРѕРґРёС‚СЃСЏ РїРѕРґРґРµСЂР¶РєР° Рё Р·РЅР°РЅРёСЏ. рџ‘‡"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("рџљЂ РџРµСЂРµР№С‚Рё Рє РєСѓСЂСЃСѓ РЅР° Boosty", url="https://boosty.to/irina_s_vitriny/posts/80389461-2021-43f0-9c20-08668971a32b?share=post_link"))
    await message.answer(text, reply_markup=keyboard)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)