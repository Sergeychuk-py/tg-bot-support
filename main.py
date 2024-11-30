import asyncio

from config import TOKEN
from handlers.custom_handlers import fms_router
from meddlewares.db import DBMiddleware
from aiogram import Bot, Dispatcher
from data.engine import sessionmarker, create_db
from handlers.default_handlers import router_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_routers(fms_router, router_handlers)


async def start_up():
    await create_db()


async def main():
    dp.startup.register(start_up)
    dp.update.middleware(DBMiddleware(sessionmarker))
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
