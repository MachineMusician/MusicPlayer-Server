from typing import Optional

from fastapi import FastAPI, File, UploadFile
from pydantic.main import BaseModel
from dataclasses import dataclass, field
from typing import List, Optional


import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pydub


app = FastAPI()

postdb = []


class Music(BaseModel):
    id: int
    title: str
    info: str
    image_link: str
    wavFile: Optional[UploadFile]

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