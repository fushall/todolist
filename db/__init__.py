from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

from settings import SQLALCHEMY_URI

engine = create_engine(
    SQLALCHEMY_URI,
    echo=True,
    poolclass=NullPool if 'sqlite' in SQLALCHEMY_URI else None
)

session = scoped_session(
    sessionmaker(bind=engine)
)

Base = declarative_base()


def auto_rollback(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError:
            session.rollback()
            raise

    return wrapper


def init_db():
    from . import user, item, item_comment

    Base.metadata.create_all(bind=engine)
