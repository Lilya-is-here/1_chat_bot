from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime)
from db import Base, engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Teller(Base):
    __tablename__ = "teller"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String())
    chat_id = Column(Integer())
    stories = relationship(
        "Story", lazy="joined"
    )

    def __repr__(self):
        return f"Teller {self.id}, {self.name}"


class Genre_list(Base):
    __tablename__ = 'genre_list'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    genre_name = Column(String())
    stories = relationship(
        "Story", lazy="joined"
    )

    def __repr__(self):
        return f"Genre {self.id}, {self.genre_name}"


class Story(Base):
    __tablename__ = 'story'

    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(
        String(), nullable=False, unique=True)
    story_text = Column(
        Text, nullable=False, unique=True)
    datetime = Column(
        DateTime(timezone=True), server_default=func.now())
    teller_id = Column(
        Integer, ForeignKey("teller.id"), index=True, nullable=False)
    genre_id = Column(
        Integer, ForeignKey("genre_list.id"), index=True, nullable=False)
    comments = relationship("Comment", back_populates="story")

    def __repr__(self):
        return f"Story {self.id}, {self.text}"


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    story_id = Column(
        Integer, ForeignKey("story.id"), primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    comment_text = Column(Text, nullable=False, unique=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    story = relationship("Story", back_populates="comments")

    def __repr__(self):
        return f"Comment {self.id}, {self.comment_text}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
