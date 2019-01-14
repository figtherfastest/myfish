from app.model.base import Base
from sqlalchemy import Column, String, SmallInteger, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(SmallInteger, primary_key=True)
    user = relationship('User')
    uid = Column(SmallInteger, ForeignKey('user.id'), nullable=False)
    wishIsbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)


