import os
from typing import Optional

from fastapi import FastAPI, File, UploadFile, Depends
from pydantic.main import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from database.database import get_db
from database.models import Music
from fastapi.middleware.cors import CORSMiddleware  # adding cors headers
import base64

from caden import inference_score
from PIL import Image

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

BASE_DIR = os.getcwd()
SOUND_DIR = os.path.join(BASE_DIR, 'output')
IMG_DIR = os.path.join(BASE_DIR, 'input')


class ResponseMusic(BaseModel):
    id: int
    title: str
    user_name: str
    description: str
    created_at: str
    image_files: str
    music_files: str

    class Config:
        orm_mode = True


class RequestMusic(BaseModel):
    title: str
    user_name: str
    description: str
    created_at: str
    image_files: List[str]


class RequestTest(BaseModel):
    test_image: str


@app.get("/")
def read_root():
    return {"Hello": "Music Player"}


@app.post("/test_img")
def test_image(req: RequestTest):
    data = req.test_image.replace(' ', '+')
    data = data.replace('.', '=')
    image_data = base64.b64decode(data)
    filename = "input/test.png"

    with open(filename, 'wb') as fh:
        fh.write(image_data)
    inference_score(f"{IMG_DIR}/test.png", "test")
    return f"{SOUND_DIR}/test.mid"


@app.get("/musics", response_model=List[ResponseMusic])
def read_musics(db: Session = Depends(get_db)):
    print(db.query(Music).first().created_at)
    musics = db.query(Music).all()
    print(musics)
    return musics


@app.post("/add_music")
def add_music(req: RequestMusic, db: Session = Depends(get_db)):
    image_list = req.image_files
    # music_list = req.music_list

    return_image_list = ""
    return_file_list = ""
    i = 1
    for image in image_list:
        data = image.replace(' ', '+')
        image_data = base64.b64decode(data)
        filename = f"input/{req.created_at}{i}" + f"{req.title}.png"

        with open(filename, 'wb') as fh:
            fh.write(image_data)
        inference_score(f"input/{req.created_at}{i}" + f"{req.title}.png",
                        f"{req.created_at}" + f"{i}" + f"{req.title}")
        return_image_list += f"{IMG_DIR}/{filename}" + ","
        return_file_list += f"{SOUND_DIR}/{req.created_at}{i}" + f"{req.title}.mid" + ","
        i += 1

    music = Music(title=req.title, user_name=req.user_name, description=req.description, created_at=req.created_at,
                  image_files=return_image_list, music_files=return_file_list)
    db.add(music)
    db.commit()

    # db.add(ImageFile(image_file=filename, music_image_id=image_id))

    # for music in music_list:
    #     db.add(MusicFile(music_file=music, music_file_id=image_id))

    db.commit()

    return req
