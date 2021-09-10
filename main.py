from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session


from database.database import get_db
from database.models import Music, MusicFile, ImageFile
from fastapi.middleware.cors import CORSMiddleware # adding cors headers

app = FastAPI()

# adding cors urls
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class ResponseMusic(BaseModel):
    id: int
    title: str
    user_name: str
    description: str
    created_at: str
    image_list: List[str]
    # wavFile: List[str]

    class Config:
        orm_mode = True


class RequestMusic(BaseModel):
    title: str
    user_name: str
    description: str
    created_at: str
    image_list: List[str]

@app.get("/")
def read_root():
    return {"Hello": "Music Player"}


@app.get("/musics", response_model=List[ResponseMusic])
def read_musics(db: Session = Depends(get_db)):
    musics = db.query(Music).all()
    return musics


@app.post("/add_music")
def add_music(req: RequestMusic, db: Session = Depends(get_db)):
    # title = req.title
    # print(**req.dict())
    # print("=====")
    # dict = {'title': req.title, 'user_name': req.user_name, 'description': req.description, 'createdAt': req.createdAt}

    music = Music(title=req.title, user_name=req.user_name, description=req.description, created_at=req.created_at)
    music_file = req.image_list
    db.add(music)

    image_id = db.query(Music).order_by(Music.id.desc()).first().id

    for value in music_file:
        db.add(ImageFile(image_file=value, music_image_id=image_id))


    db.commit()
    return music
