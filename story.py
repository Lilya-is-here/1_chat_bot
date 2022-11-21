from telegram import ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from db_query import cursor_teller, get_or_create_genre, get_or_create_story



def story_start(update, context):
    update.message.reply_text(
        "Привет, как вас зовут? Как называется ваша история?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def teller_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и название истории")
        return "name"
    else:
        context.user_data["story"] = {"name": user_name}
        update.message.reply_text(
            "Пожалуйста, введите жанр истории."
        )
        return "genre"


def story_genre(update, context):
    context.user_data["story"]["genre"] = update.message.text
    get_or_create_genre(cursor_teller,
                        context.user_data["story"]["genre"])
    update.message.reply_text("Напишите свою историю.")
    return "text"


def story_text(update, context):
    context.user_data['story']["text"] = update.message.text
    
    get_or_create_story(cursor_teller,
                        context.user_data["story"]["text"])
    user_text = format_story(context.user_data["story"])
    update.message.reply_text(user_text, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def format_story(story):
    user_text = f""" <b>Имя Название </b>: {story["name"]}
                      <b>Жанр</b>: {story["genre"]}
                      <b>История</b>: {story["text"]}
                      """
    return user_text


def story_dont_know(update, context):
    update.message.reply_text('Я вас не понимаю.')
