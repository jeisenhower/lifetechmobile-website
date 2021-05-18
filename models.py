from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime

Base = declarative_base()


class Quotes(Base):
    __tablename__ = "quotes"
    id = Column(Integer, unique=True, autoincrement=True, index=True, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    message = Column(Text)
    creation_time = Column(DateTime)


class NewsLetterSubs(Base):
    __tablename__ = "newsletter_subs"
    id = Column(Integer, unique=True, autoincrement=True, index=True, primary_key=True)
    email = Column(String(50))
    creation_time = Column(DateTime)
