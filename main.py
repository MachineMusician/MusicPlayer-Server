from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel


class PostInputRequest(BaseModel):
    title: str
    info: str
    imageURL: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
