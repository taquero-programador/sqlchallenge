#!/usr/bin/env python3

# from typing import List, Union # on python3.10 no required
from pydantic import BaseModel
from datetime import date, datetime


class MembersCreate(BaseModel):
    customer_id: str
    join_date: datetime


# response_model
class Members(MembersCreate):
    #customer_id: str
    join_date: datetime

    class Confing:
        orm_mode = True


class MenuCreate(BaseModel):
    product_name: str
    price: float


# response_model
class Menu(MenuCreate):
    product_name: str
    price: float

    class Confing:
        orm_mode = True
