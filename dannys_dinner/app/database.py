#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATEBASE_URL = "mysql+pymysql://{}:{}@{}/bender?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATEBASE_URL.format(
    settings.user_db,
    settings.pass_db.get_secret_value(),
    settings.url_db
    ))

SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()

