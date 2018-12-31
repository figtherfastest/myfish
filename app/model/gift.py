from sqlalchemy import Column, SmallInteger, Integer, ForeignKey, Boolean, String, Text
from sqlalchemy.orm import relationship
from app.model.base import Base


class Gift(Base):
    giftId = Column(SmallInteger, primary_key=True)
    id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    bookIsbn = Column(String(13))
    launched = Column(Boolean,  default=False)