import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

challenges = [
    "Сделай фото чего-то странного на улице.",
    "Напиши себе письмо в будущее.",
    "Похвали кого-то в комментариях.",
    "Танцуй под любимую песню 3 минуты.",
    "Не пользуйся соцсетями 2 часа.",
    "Позвони старому другу и просто поболтай.",
    "Погугли новую для себя тему и выучи 3 факта."
 

]

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Получить челлендж"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот случайных челленджей. Жми на кнопку и делай день интереснее!",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "Получить челлендж")
async def send_challenge(message: types.Message):
    challenge = random.choice(challenges)
    await message.answer(f"Твой челлендж на сегодня:\n\n*{challenge}*", parse_mode="Markdown")

if name == '__main__':
    executor.start_polling(dp)
