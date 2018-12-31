from app.model.base import Base
from sqlalchemy import Column, String, SmallInteger, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Wish(Base):
    wishId = Column(SmallInteger, primary_key=True)
    user = relationship('User')
    id = Column(SmallInteger, ForeignKey('user.id'), nullable=False)
    wishIsbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)


