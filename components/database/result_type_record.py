from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from database import Base


class ResultTypeRecord(Base):
    __tablename__ = "result_type"
    id = Column(Integer, primary_key=True)
    result_type = Column(String, nullable=False)
