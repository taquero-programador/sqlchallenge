#!/urs/bin/env python3

from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Name(Base):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True, index=True)
    name_one = Column(String(20), index=True)
