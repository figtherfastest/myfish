from sqlalchemy import Column, Integer, String, SmallInteger
from app.model.base import Base, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.libs.error_code import AuthFailed
from app.libs.helper import is_isbn_or_key
from app.model.gift import Gift
from app.model.wish import Wishes



class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128), nullable=False)

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def reset_by_email(user, secret):
        with db.auto_commit():
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'id': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @staticmethod
    def can_save_to_list(isbn, user_id):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        gift = Gift.query.filter_by(id=user_id, bookIsbn=isbn, launched=False).first()
        wish = Wishes.query.filter_by(id=user_id, wishIsbn=isbn, launched=False).first()
        if not gift and not wish:
            return True
        else:
            return False
