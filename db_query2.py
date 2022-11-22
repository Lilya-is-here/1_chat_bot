from db import db_session
from models import Teller, Genre_list


def get_or_create_user(chat_id_bot, effective_user):
    user = db_session.query(
        Teller.chat_id).filter_by(
            chat_id=chat_id_bot).first()
    if not user:
        teller = Teller(name=effective_user.username, chat_id=chat_id_bot)
        db_session.add(teller)
        db_session.commit()
        return


def get_or_create_genre(genre_bot):
    genre = db_session.query(
        Genre_list.genre_name).filter_by(
            genre_name=genre_bot).first()
    if not genre:
        genre = Genre_list(genre_name=genre_bot)
        db_session.add(genre)
        db_session.commit()
        return
   
#def get_or_create_story(cursor_teller, story_text):
    #story = cursor_teller.execute(
       # f"SELECT story_text FROM story WHERE story_text = '{story_text}'"
       # )
   # if not story:
       # print("No story")
      #  story = '''
       # INSERT INTO story (teller(teller_id), genre_list(genre_id), story_text,datetime) VALUES (%s, %s, %s,NOW())'''
      #  cursor_teller.execute(story, ([story_text], ))
   # sql1 = '''select * from story;'''
    #cursor_teller.execute(sql1)
    #for i in cursor_teller.fetchall():
   #     print(i)
   # conn.commit()
   # conn.close()
   # return

   




