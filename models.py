from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from db import Base, engine


class Teller(Base):
    __tablename__ = "teller"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    chat_id = Column(Integer())

    def __repr__(self):
        return f"Teller {self.id}, {self.name}"


class Genre_list(Base):
    __tablename__ = 'genre_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String())

    def __repr__(self):
        return f"Genre {self.id}, {self.genre_name}"


class Story(Base):
    __tablename__ = 'story'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teller_id = Column(Integer, ForeignKey('teller.id'), nullable=False)
    genre_id = Column(Integer, ForeignKey('genre_list.id'), nullable=False)
    title = Column(String(), nullable=False)
    story_text = Column(Text, nullable=False)
    datetime = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"Story {self.id}, {self.title}"


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    comment_text = Column(Text, nullable=False)
    datetime = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"Comment {self.id}, {self.comment_text}"


class Story_comment(Base):
    __tablename__ = 'story_comment'

    story_id = Column(Integer, ForeignKey('story.id'), primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'),  primary_key=True)

    def __repr__(self):
        return f"Story_comment {self.story_id}, {self.comment_id}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
