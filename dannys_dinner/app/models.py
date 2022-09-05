#!/urs/bin/env python3

from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Members(Base):
    __tablename__ = "members"

    customer_id = Column(String(1), primary_key=True)
    join_date = Column(Date)

