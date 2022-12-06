from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from db_query import choose_genre


def read_start(update, context):
    update.message.reply_text(
        "Привет, какой жанр вас интересует?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "genre"


def read_genre(update, context):
    genre = update.message.text
    context.user_data["read"] = {"genre": genre}
    choose_genre(context.user_data["read"]["genre"], update)
    update.message.reply_text("Напишите комментарий.")
    return "text"


def read_text(update, context):
    context.user_data["read"]["text"] = update.message.text
    return ConversationHandler.END


def story_dont_know(update, context):
    update.message.reply_text('Я вас не понимаю.')
