from flask_login.mixins import UserMixin
from sqlalchemy import Column, String, Integer, Sequence
from werkzeug.security import generate_password_hash, check_password_hash

from . import Base, session


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    password_prompt = Column(String(64), default='')

    def set_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def get_user(user_id):
    return session.query(User).get(user_id)


def create_user(username, password, password_prompt=''):
    user = User(username=username, password_prompt=password_prompt)
    user.set_password(password)
    session.add(user)
    session.commit()
    return True
