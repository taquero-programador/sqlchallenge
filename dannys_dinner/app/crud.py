#!/urs/bin/env python3

from sqlalchemy.orm import Session
from . import models, schemas

def create_member(db: Session, user: schemas.Members, id_user: str):
    db_user = models.Members(customer_id=id_user, join_date=user.join_date)
    db.add(db_user)
    db.refresh(db_user)
    return db_user

def validate_user(db: Session, id_user: str):
    return db.query(models.Members).filter(models.Members.customer_id==id_user).first()
