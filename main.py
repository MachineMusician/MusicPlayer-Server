from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session


from database.database import get_db
from database.models import Music

app = FastAPI()


class ResponseMusic(BaseModel):
    id: int
    title: str
    info: str
    image_link: str
    wavFile: Optional[bytes]

    class Config:
        orm_mode = True


class RequestMusic(BaseModel):
    title: str
    info: str
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
