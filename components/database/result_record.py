from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from database import Base


class ResultRecord(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("card.id"), nullable=False)
    result_type_id = Column(Integer, ForeignKey("result_type.id"), nullable=False)
    smilies = Column(Integer)
    effect = Column(String)
    gossip = Column(Integer)
