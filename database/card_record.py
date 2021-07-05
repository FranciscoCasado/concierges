from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from database import Base


class CardRecord(Base):
    __tablename__ = "card"
    id = Column(Integer, ForeignKey("deck.id"), primary_key=True)
    deck_id = Column(Integer, nullable=False)
    content = Column(String)
    points = Column(Integer, nullable=True)
    diligent_dice = Column(Integer, ForeignKey("dice.id"), nullable=True)
    lazy_dice = Column(Integer, ForeignKey("dice.id"), nullable=True)
