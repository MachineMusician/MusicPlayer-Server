from fastapi import FastAPI, Depends, Path, HTTPException
from sqlalchemy.orm import Session

from main import app
from . import models, database


@app.get(path="/api/music/readAll")
def getAll(
        db: Session = Depends(database.get_db())):
    result = db.query(models.Music)

    if result is None:
        raise HTTPException(status_code=404, detail="조회할 데이터가 없습니다.")

    return {
        "status": "OK",
        "data": result
    }