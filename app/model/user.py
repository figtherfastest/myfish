from sqlalchemy import Column, Integer, String
from app.model.base import Base
from werkzeug.security import generate_password_hash

class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)