#!/urs/bin/env python3

from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.Members).filter(models.Members.customer_id == user_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Members).offset(skip).limit(limit).all()


def create_member(db: Session, user: schemas.MembersCreate):
    db_user = models.Members(customer_id=user.customer_id.upper(), join_date=user.join_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def validate_user(db: Session, user_id: str):
    return db.query(models.Members).filter(models.Members.customer_id==user_id).first()
