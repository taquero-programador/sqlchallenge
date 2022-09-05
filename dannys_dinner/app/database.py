#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings, SecretStr, Field

class Settings(BaseSettings):
    url_db: str = Field(..., env="url_database")
    user_db: str = Field(..., env="user_db")
    pass_db: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


print(Settings())

SQLALCHEMY_DATEBASE_URL = ""
