from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary, BINARY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .database import Base
from . import database
from pydantic import BaseModel
from typing import List, Optional


class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    info = Column(String, nullable=False)
    image_link = Column(String)
    wavFile = Column(LargeBinary)