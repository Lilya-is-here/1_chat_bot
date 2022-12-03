from db import db_session
from models import Teller, Genre_list, Story


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


def get_or_create_story(story_title_bot, story_text_bot):
    story_bot = db_session.query(
        Story.title, Story.story_text,
        Story.teller_id, Story.genre_id).filter_by(
            title=story_title_bot, story_text=story_text_bot,
            teller_id=Teller.id, genre_id=Genre_list.id).first()
    if not story_bot:
        story_bot = Story(
                          title=story_title_bot,
                          story_text=story_text_bot,
                         )
        db_session.add(story_bot)
        db_session.commit()
        return
