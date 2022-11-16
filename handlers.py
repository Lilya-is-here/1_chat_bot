from utils import main_keyboard
from db_query import cursor_teller, get_or_create_user


def greet_user(update, context):
    print("Вызван старт")
    update.message.reply_text(
                              "Привет! Я создал этот чат для ваших историй."
                              " Хотите поделиться историей? Нажмите 'Story'."
                              " Хотите читать истории? Нажмите 'Read'",
                              reply_markup=main_keyboard())
    get_or_create_user(cursor_teller,
                       update.effective_user, update.message.chat.id)
