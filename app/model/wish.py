from app.model.base import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Wishes(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    wishIsbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)

    def keys(self):
        return ['id', 'uid', 'wishIsbn', 'binding', 'launched']



