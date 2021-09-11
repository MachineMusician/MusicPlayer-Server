from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary, BINARY, BLOB
from sqlalchemy.orm import relationship
from .database import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    image_files = Column(String)
    music_files = Column(String)

    def __init__(self, title: str, user_name: str, description: str, created_at: str, image_files: str, music_files: str):
        self.title = title
        self.user_name = user_name
        self.description = description
        self.created_at = created_at
        self.image_files = image_files
        self.music_files = music_files


# class MusicFile(Base):
#     __tablename__ = "musicfile"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
#     music_file = Column(String, nullable=False)
#     music_file_id = Column(Integer, nullable=False)
#
#     def __init__(self, music_file: str, music_file_id: int):
#         self.music_file = music_file
#         self.music_file_id = music_file_id
#
#
# class ImageFile(Base):
#     __tablename__ = "imagefile"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
#     image_file = Column(String, nullable=False)
#     music_image_id = Column(Integer)
#
#     def __init__(self, image_file: str, music_image_id: int):
#         self.image_file = image_file
#         self.music_image_id = music_image_id

