from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models.base import Base


class DeckRecord(Base):
    __tablename__ = "deck"
    id = Column(Integer, primary_key=True)
    deck_name = Column(String, nullable=False)
