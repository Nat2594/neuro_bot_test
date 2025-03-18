import asyncio
import logging

from aiogram import Bot, Dispatcher
import config
from handlers import common, career_choice


# Основная функция запуска бота
async def main():
    API_TOKEN = config.token

    # Настраиваем логирование
    logging.basicConfig(level=logging.INFO)

    # Создаем экземпляры бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)


    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
