from aiogram import Bot, Dispatcher
import asyncio
import logging
from environs import Env
from app import handlers
from app import set_main_menu


class BotRun:
    async def main(self):
        env = Env()
        env.read_env()
        bot = Bot(token=env("BOT_TOKEN"))
        dp = Dispatcher(storage=handlers.storage)
        dp.include_router(handlers.router)
        dp.startup.register(set_main_menu)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == "__main__":
    bot_run = BotRun()
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )
    try:
        asyncio.run(bot_run.main())
    except:
        print("Завершено")
        KeyboardInterrupt()
