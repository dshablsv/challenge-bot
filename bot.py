
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.webhook import get_new_configured_app
from aiohttp import web

API_TOKEN = os.getenv("API_TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")  # например: https://challenge-bot.onrender.com
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

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

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

# Для Render: запуск сервера
if name == '__main__':
    port = int(os.environ.get('PORT', 8000))
    web.run_app(app, host='0.0.0.0', port=port)
