from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from pydub import AudioSegment


출처: https://deepinlife.tistory.com/20 [나의 이야기]

app = FastAPI()

postdb = []


class Music(BaseModel):
    id: int
    title: str
    info: str
    image_link: str
    wavFile:

@app.get("/")
def read_root():
    return {"Hello": "Music Player"}


@app.get("/musics")
def read_musics():
    return postdb

@app.post("/add_music")
def add_music(music: Music):
    postdb.append(music)
    return postdb[-1]