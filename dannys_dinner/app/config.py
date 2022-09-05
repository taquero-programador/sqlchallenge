#!/usr/bin/env python3

from pydantic import BaseSettings, Field, SecretStr

class Settings(BaseSettings):
    url_db: str = Field(..., env="url_database")
    user_db: str = Field(..., env="user_db")
    pass_db: SecretStr = Field(..., env="pass_db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

