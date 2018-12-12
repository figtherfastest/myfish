from sqlalchemy import Column, Integer, String, SmallInteger
from app.model.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from app.lib.error_code import AuthFailed

class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid': user.id}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)