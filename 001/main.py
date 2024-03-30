from aiogram import Dispatcher, Bot, types
from asyncio import run

API_TOKEN = "token"
dp = Dispatcher()
bot = Bot(API_TOKEN)


async def echo(message: types.Message):
    await message.reply(message.text)


async def start():
    dp.message.register(echo)
    await dp.start_polling(bot)


run(start())
