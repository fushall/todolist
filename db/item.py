from datetime import datetime

from sqlalchemy import Column, String, Integer, Sequence, DateTime, Text

from . import Base, session


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    user_id = Column(Integer)
    title = Column(String(64))
    video_url = Column(String(512))
    markdown = Column(Text)
    done = Column(Integer, default=0)
    created_at = Column(DateTime)


def create_item(title, video_url='', markdown='', user=None):
    item = Item(
        title=title,
        video_url=video_url,
        markdown=markdown,
        created_at=datetime.now(),
        user_id=user.id if user else None
    )
    session.add(item)
    session.commit()


def find_user_item(user, item_id):
    return session.query(Item) \
        .filter_by(user_id=user.id, id=item_id) \
        .first()


def find_user_undone_items(user):
    return session.query(Item) \
        .filter_by(user_id=user.id) \
        .filter(Item.done == 0) \
        .order_by(Item.created_at.desc()) \
        .all()


def find_user_done_items(user):
    return session.query(Item) \
        .filter_by(user_id=user.id) \
        .filter(Item.done > 0) \
        .order_by(Item.created_at.desc()) \
        .all()


def get_user_item_detail(user, item_id):
    return session.query(Item) \
        .filter_by(user_id=user.id, id=item_id) \
        .first()


def delete_user_item(user, item_id):
    item = session.query(Item) \
        .filter_by(user_id=user.id, id=item_id) \
        .first()
    if item:
        session.delete(item)
        session.commit()
        return True


def done_user_item(user, item_id):
    item = session.query(Item) \
        .filter_by(user_id=user.id, id=item_id) \
        .first()
    if item:
        item.done += 1
        session.commit()
        return True
