from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Music, MusicFile, ImageFile
from fastapi.middleware.cors import CORSMiddleware  # adding cors headers
import base64

from caden import inference_score

app = FastAPI()
# inference_score("resources/samples/mary.jpg")  # img path
# adding cors urls
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class ResponseMusic(BaseModel):
    id: int
    title: str
    user_name: str
    description: str
    created_at: str
    image_list: List[str]
    music_list: List[str]

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
    music = Music(title=req.title, user_name=req.user_name, description=req.description, created_at=req.created_at)
    image_list = req.image_list
    # music_list = req.music_list
    db.add(music)
    db.commit()

    image_id = db.query(Music).order_by(Music.id.desc()).first().id

    for image in image_list:
        data = image.replace(' ', '+')
        image_data = base64.b64decode(data)
        filename = f"input/{image_id}" + f"{req.title}.png"
        with open(filename, 'wb') as fh:
            fh.write(image_data)
        db.add(ImageFile(image_file=image, music_image_id=image_id))

    print(f"input/{image_id}" + f"{req.title}")

    inference_score("resources/samples/mary.jpg", f"{image_id}" + f"{req.title}")
    # for music in music_list:
    #     db.add(MusicFile(music_file=music, music_file_id=image_id))

    db.commit()

    return req
