from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/MusicPlayer')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))