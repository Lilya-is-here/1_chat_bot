from utils import main_keyboard

def greet_user(update, context):
    print("Вызван старт")
    
    update.message.reply_text("Привет! Я создал этот чат для того, чтобы делиться историями. Если хотите поделиться историей, нажмите 'Story'. Если хотите ознакомиться с истроиями других людей нажмите 'Read'", reply_markup = main_keyboard())
