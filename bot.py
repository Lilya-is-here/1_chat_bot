import logging
from telegram.ext import Updater, CommandHandler
import settings

logging.basicConfig(filename = "bot.log", level = logging.INFO)

PROXY = {"proxy_url":settings.PROXY_URL,
           "urlib3_proxy_kwargs": {"username": settings.PROXY_USERNAME, "password":settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван старт")
    update.message.reply_text("Привет! Я создал этот чат для того, чтобы делиться историями.")


def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()