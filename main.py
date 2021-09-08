from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session


from database.database import get_db
from database.models import Music
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
    info: str
    nickname: str
    image_link: str
    wavFile: Optional[bytes]

    class Config:
        orm_mode = True


class RequestMusic(BaseModel):
    title: str
    info: str
    nickname: str
    image_link: str

@app.get("/")
def read_root():
    return {"Hello": "Music Player"}


@app.get("/musics", response_model=List[ResponseMusic])
def read_musics(db: Session = Depends(get_db)):
    musics = db.query(Music).all()
    return musics


@app.post("/add_music")
def add_music(req: RequestMusic, db: Session = Depends(get_db)):
    music = Music(**req.dict())
    db.add(music)
    db.commit()
    return music
