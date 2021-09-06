from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from dataclasses import dataclass, field
from typing import List, Optional
from sqlalchemy.orm import Session


import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pydub

from database.database import get_db
from database.models import Music

app = FastAPI()



class ResponseMusic(BaseModel):
    id: int
    title: str
    info: str
    image_link: str
    wavFile: Optional[UploadFile]

@app.get("/")
def read_root():
    return {"Hello": "Music Player"}


@app.get("/musics", response_model=List[ResponseMusic])
def read_musics(db: Session = Depends(get_db)):
    musics = db.query(Music).all()
    return musics

@app.post("/add_music")
def add_music(music: Music):
    postdb.append(music)
    return postdb[-1]