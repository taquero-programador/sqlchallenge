#!/usr/bin/env python3

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
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
def create_member(user: schemas.MembersCreate, db: Session = Depends(get_db)):
    db_user = crud.validate_user(db, user_id=user.customer_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists!")
    return crud.create_user(db=db, user=user)


@app.get("/menu/{product_name}")
def read_item(product_name: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, product_name=product_name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found!")
    return item


@app.get("/menu/")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_items(db=db, skip=skip, limit=limit)


@app.post("/menu/")
def create_item(item: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_item = crud.validate_item(db, product_name=item.product_name)
    if db_item:
        raise HTTPException(status_code=400, detail="Menu already exists!")
    return crud.create_item(db, item=item)
