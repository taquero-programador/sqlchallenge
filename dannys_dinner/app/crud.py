#!/urs/bin/env python3

from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.Members).filter(models.Members.customer_id == user_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Members).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.MembersCreate):
    db_user = models.Members(customer_id=user.customer_id.upper(),
                             join_date=user.join_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def validate_user(db: Session, user_id: str):
    return db.query(models.Members).filter(models.Members.customer_id==user_id).first()


def get_item(db: Session, product_name: str):
    return db.query(models.Menu).filter(models.Menu.product_name==product_name).first()


def get_all_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Menu).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.MenuCreate):
    db_item = models.Menu(product_name=item.product_name.upper(),
                          price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def validate_item(db: Session, product_name: str):
    return db.query(models.Menu).filter(models.Menu.product_name==product_name).first()

