#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings

url_db = Settings().url_db
user = Settings().user_db
passw = Settings().pass_db
print(url_db)

SQLALCHEMY_DATEBASE_URL = "mysql+pymysql://user:passw@url_db/bender"

engine = create_engine(SQLALCHEMY_DATEBASE_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()

