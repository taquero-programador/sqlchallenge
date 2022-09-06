#!/usr/bin/env python3

# from typing import List, Union # on python3.10 no required
from pydantic import BaseModel
from datetime import date, datetime

class Members(BaseModel):
    id: int
    join_date: datetime

    class Config:
        ord_mode = True
