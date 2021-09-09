from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary, BINARY, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    info = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    image_link = Column(String)
    wavFile = Column(LargeBinary().with_variant(BLOB, "mysql"))

class MusifFile(Base):
    __tablename__ = "musicfile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    image_file = Column(LargeBinary().with_variant(BLOB, "mysql"), nullable=False)
    dashboard_id = Column(Integer, nullable=False)