import logging
from telegram.ext import Updater, CommandHandler
from handlers import greet_user

import settings

logging.basicConfig(filename = "bot.log", level = logging.INFO)

PROXY = {"proxy_url":settings.PROXY_URL,
           "urlib3_proxy_kwargs": {"username": settings.PROXY_USERNAME, "password":settings.PROXY_PASSWORD}}


def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()