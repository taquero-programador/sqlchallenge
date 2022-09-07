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


@app.get("/members/{user_id}")
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return user


@app.get("/members/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users


@app.post("/members/")
def create_members(user: schemas.Members, db: Session = Depends(get_db)):
    db_user = crud.validate_user(db, user_id=user.customer_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Member already exist")
    return crud.create_member(db=db, user=user)

