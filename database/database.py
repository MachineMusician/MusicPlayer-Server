from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import logging

# 환경 변수로 설정 필요
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/MusicPlayer"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
