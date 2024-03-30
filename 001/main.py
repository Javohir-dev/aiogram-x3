from aiogram import Dispatcher, Bot, types
from asyncio import run

API_TOKEN = "6434489869:AAEESi6PoTKyr6U9nP6ceMKk8tiB6A8TWUQ"
dp = Dispatcher()
bot = Bot(API_TOKEN)


async def echo(message: types.Message):
    await message.reply(message.text)


async def start():
    dp.message.register(echo)
    await dp.start_polling(bot)


run(start())
