from email import message_from_string

from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox

router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.chat.first_name
    await message.answer(F'Привет, {name}', reply_markup=kb1)

# Хэндлер на команду /stop
@router.message(Command('stop'))
async def stop_handler(message: types.Message):
    name = message.chat.first_name
    await message.answer(F'bye, {name}')


# Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(F.text.lower() == 'show fox')
async def send_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'look, fox {name}')
    await message.answer_photo(photo=img_fox)


# Эхо-ответ на любое сообщение
@router.message(F.text)
async def echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'ура' in message.text:
        await message.answer("Ураа")
    elif message.text == "info":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)


