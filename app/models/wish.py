from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from .base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False )