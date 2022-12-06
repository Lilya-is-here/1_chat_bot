import logging
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, ConversationHandler)
from handlers import greet_user
from story import (story_start, teller_name,
                   story_genre, story_text, story_dont_know, story_title)
from read import (read_start, read_genre, read_text)
import settings

# pip freeze > requirements.txt

logging.basicConfig(filename="bot.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

PROXY = {"proxy_url": settings.PROXY_URL,
         "urlib3_proxy_kwargs": {"username": settings.PROXY_USERNAME,
                                 "password": settings.PROXY_PASSWORD}}


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    story = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Рассказать историю)$'),
                           story_start)
        ],
        states={
            "name": [MessageHandler(Filters.text, teller_name)],
            "title": [MessageHandler(Filters.text, story_title)],
            "genre": [MessageHandler(Filters.text, story_genre)],
            "text": [MessageHandler(Filters.text, story_text)],
        },
        fallbacks=[
            MessageHandler(
                Filters.text |
                Filters.photo |
                Filters.video |
                Filters.document |
                Filters.location, story_dont_know)
        ]
        )

    read = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Читать истории)$'),
                           read_start)
        ],
        states={
            "genre": [MessageHandler(Filters.text, read_genre)],
            "text": [MessageHandler(Filters.text, read_text)],
            # "comment": [MessageHandler(Filters.text, comment_text)],
        },
        fallbacks=[
            MessageHandler(
                Filters.text |
                Filters.photo |
                Filters.video |
                Filters.document |
                Filters.location, story_dont_know)
        ]
        )

    dp.add_handler(story)
    dp.add_handler(read)
    dp.add_handler(CommandHandler("start", greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
