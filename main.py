from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel


app = FastAPI()

postdb = []


class Music(BaseModel):
    id: int
    title: str
    info: str
    image_link: str

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