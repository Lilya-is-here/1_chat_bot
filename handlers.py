from utils import main_keyboard
from db_query2 import get_or_create_user
from db import db_session


def greet_user(update, context):
    print("Вызван старт")
    update.message.reply_text(
                              "Привет! Я создал этот чат для ваших историй."
                              " Хотите поделиться историей? Нажмите 'Story'."
                              " Хотите читать истории? Нажмите 'Read'",
                              reply_markup=main_keyboard())
    get_or_create_user(
                       update.message.chat.id, update.effective_user)
