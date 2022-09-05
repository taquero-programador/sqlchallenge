#!/urs/bin/env python3

from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Members(Base):
    __tablename__ = "members"

    customer_id = Column(String(1), primary_key=True)
    join_date = Column(Date)

    sales = relationship("Sales", back_populates="memb")


class Menu(Base):
    __tablename__ = "menu"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(20))
    price = Column(Boolean)

    sales = relationship("Sales", back_populates="mn")


class Sales(Base):
    __tablename__ = "sales"

    customer_id = Column(String, ForeignKey("members.customer_id"))
    order_date = Column(DateTime)
    product_id = Column(Integer, ForeignKey("menu.product_id"))

    memb = relationship("Members", back_populates="sales")
    mn = relationship("Menu", back_populates="sales")
