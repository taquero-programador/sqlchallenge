#!/urs/bin/env python3

from sqlalchemy import (Float, Column,
                        ForeignKey, String,
                        Integer, Date, DateTime)
from sqlalchemy.orm import relationship
from .database import Base

class Members(Base):

    __tablename__ = "members"

    customer_id = Column(String(1), primary_key=True)
    join_date = Column(Date, nullable=False)

    sales = relationship("Sales")


class Menu(Base):

    __tablename__ = "menu"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(20))
    price = Column(Float, nullable=False)

    sales = relationship("Sales")


class Sales(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    customer_id = Column(String(1), ForeignKey("members.customer_id"))
    order_date = Column(DateTime, nullable=False)
    product_id = Column(Integer, ForeignKey("menu.product_id"))

