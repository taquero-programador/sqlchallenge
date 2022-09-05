#!/usr/bin/env python3

import os
from pydantic import BaseSettings, Field, SecretStr
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    # url_db: str = Field(..., env="url_database")
    url_db: str = os.getenv("url_database")
    user_db: str = os.getenv("user_db")
    pass_db: SecretStr = os.getenv("pass_db")

    class Config:
        env_prefix = ""
        case_sensite = False
        env_file = "~/.env"
        env_file_encoding = "utf-8"

settings = Settings()

