from telegram import ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from db_query import (get_or_create_story, get_or_create_genre)


def story_start(update, context):
    update.message.reply_text(
        "Привет, как вас зовут?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def teller_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста, введите имя")
        return "name"
    else:
        context.user_data["story"] = {"name": user_name}
        update.message.reply_text(
            "Пожалуйста, введите название истории."
        )
        return "title"


def story_title(update, context):
    context.user_data["story"]["title"] = update.message.text
    update.message.reply_text(
            "Пожалуйста, введите жанр истории."
        )
    return "genre"


def story_genre(update, context):
    context.user_data["story"]["genre"] = update.message.text
    update.message.reply_text("Напишите свою историю.")
    return "text"


def story_text(update, context):
    context.user_data['story']["text"] = update.message.text
    
    user_text = format_story(context.user_data["story"])

    update.message.reply_text(user_text, parse_mode=ParseMode.HTML)
    story_dict = context.user_data
    print(story_dict)
    get_or_create_genre(context.user_data["story"]["genre"])
    get_or_create_story(context.user_data["story"]["title"],
                        context.user_data["story"]["text"],
                        context.user_data["story"]["genre"],
                        update.effective_user
                        )
   
    
   
   
    return ConversationHandler.END


def format_story(story):
    user_text = f""" <b>Имя Название </b>: {story["name"]}
                      <b>Жанр</b>: {story["genre"]}
                      <b>История</b>: {story["text"]}
                      """
    return user_text


def story_dont_know(update, context):
    update.message.reply_text('Я вас не понимаю.')
