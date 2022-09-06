#!/urs/bin/env python3

from sqlalchemy.orm import Session
from . import models, schemas

def create_member(db: Session, user: schemas.Members):
    db_user = models.Members(customer_id=user.customer_id, join_date=user.join_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def validate_user(db: Session, id_user: str):
    return db.query(models.Members).filter(models.Members.customer_id==id_user).first()
