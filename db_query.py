import psycopg2
import settings

conn = psycopg2.connect(
        database="teller",
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port
    )

conn.autocommit = True

cursor_teller = conn.cursor()


def get_or_create_user(cursor_teller, effective_user, chat_id):
    user = cursor_teller.execute(
        f"SELECT chat_id FROM teller WHERE chat_id = {chat_id}"
        )
    user = cursor_teller.fetchone()
    if not user:
        print("No user")
        user = """
        INSERT INTO teller (teller_name, chat_id) VALUES (%s,%s)"""
        cursor_teller.execute(user, (effective_user.username, chat_id))
    sql1 = '''select * from teller;'''
    cursor_teller.execute(sql1)
    for i in cursor_teller.fetchall():
        print(i)
    conn.commit()

    return


def get_or_create_genre(cursor_teller, genre_name):
    name_of_genre = cursor_teller.execute(
        f"SELECT genre FROM genre_list WHERE genre = '{genre_name}'"
        )
    name_of_genre = cursor_teller.fetchone()
    if not name_of_genre:
        print("No genre")
        name_of_genre = '''
        INSERT INTO genre_list (genre) VALUES (%s)'''
        cursor_teller.execute(name_of_genre, ([genre_name]))
    sql1 = '''select * from genre_list;'''
    cursor_teller.execute(sql1)
    for i in cursor_teller.fetchall():
        print(i)
    conn.commit()
    conn.close()
    return
