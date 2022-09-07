#!/usr/bin/env python3

# from typing import List, Union # on python3.10 no required
from pydantic import BaseModel
from datetime import date, datetime


class Members(BaseModel):
    customer_id: str
    join_date: datetime


# response_model
class MembersCreate(Members):
    customer_id: str
    join_date: datetime

    class Confing:
        orm_mode = True


class Menu(BaseModel):
    product_name: str
    price: float


class MenuCreate(Menu):
    product_name: str
    price: float

    class Confing:
        orm_mode = True
