#!/usr/bin/env python3

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/members/")
def create_members(mem: schemas.Members, db: Session = Depends(get_db)):
    db_user = crud.validate_user(db, id_user=mem.customer_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Member already exist")
    return crud.create_member(db=db, user=mem)
