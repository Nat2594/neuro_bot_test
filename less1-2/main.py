import asyncio
import logging
from idlelib.pyshell import usage_msg

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
import config
from keyboards import kb1, kb2
from random_fox import fox
from random import randint

API_TOKEN = config.token

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.chat.first_name
    await message.answer(F'Привет, {name}', reply_markup=kb1)

# Хэндлер на команду /stop
@dp.message(Command('stop'))
async def stop_handler(message: types.Message):
    name = message.chat.first_name
    await message.answer(F'bye, {name}')


# Хэндлер на команду /fox
@dp.message(Command('fox'))
@dp.message(F.text.lower() == 'show fox')
async def send_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'look, fox {name}')
    await message.answer_photo(photo=img_fox)


# Эхо-ответ на любое сообщение
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(F'привет-Привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(F'пока-Пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎳")
    elif 'fox' in msg_user:
        await message.answer(f'look what I have, {name}', reply_markup=kb2)
    else:
        await message.answer(F'Я не знаю такого слова')

# Основная функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
