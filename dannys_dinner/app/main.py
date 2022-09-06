#!/usr/bin/env python3

import models as md
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from database import SessionLocal, engine

md.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/members/", reponse_models=schemas.Members)
def create_members(mem: schemas.Members, db: Session = Depends(get_db)):
    db_user = crud.validate_user(db, id_user=mem.customer_id)
    if db_user:
        raise HTTPException(status_code=400, datail="Member already exist")
    return crud.create_member(db=db, user=mem)
