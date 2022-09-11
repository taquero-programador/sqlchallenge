#!/usr/bin/env python3

import os
from pydantic import BaseSettings, Field, SecretStr
from dotenv import load_dotenv


class Settings(BaseSettings):
    load_dotenv()
    # url_db: str = Field(..., env="url_database")
    # url_db: str = os.getenv("url_database")
    url_db: str = os.environ["URL_DATABASE"]
    user_db: str = os.environ["USER_DB"]
    pass_db: SecretStr = os.environ["PASS_DB"]

    class Config:
        env_prefix = ""
        case_sensite = False
        env_file = "~/.env"
        env_file_encoding = "utf-8"

settings = Settings()
