from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models.base import Base


class DiceRecord(Base):
    __tablename__ = "dice"
    id = Column(Integer, primary_key=True)
    dice_name = Column(String, nullable=False)
