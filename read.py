from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler


def read_start(update, context):
    update.message.reply_text(
        "Привет, какой жанр вас интересует?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "genre"


def read_genre(update, context):
    context.user_data["read"]["genre"] = update.message.text
    return ConversationHandler.END


def story_dont_know(update, context):
    update.message.reply_text('Я вас не понимаю.')
