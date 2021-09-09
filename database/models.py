from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary, BINARY, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    createdAt = Column(String, nullable=False)


class MusifFile(Base):
    __tablename__ = "musicfile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    music_file = Column(LargeBinary().with_variant(BLOB, "mysql"), nullable=False)
    music_id = Column(Integer, ForeignKey('music.id'), nullable=False)


class ImageFile(Base):
    __tablename__ = "imagefile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    image_file = Column(LargeBinary().with_variant(BLOB, "mysql"), nullable=False)
    music_id = Column(Integer, ForeignKey('music.id'), nullable=False)
