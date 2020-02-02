from datetime import datetime

from sqlalchemy import Column, String, Integer, Sequence, DateTime

from . import Base, session, auto_rollback


class ItemComment(Base):
    __tablename__ = 'item_comments'

    id = Column(Integer, Sequence('item_comment_id_seq'), primary_key=True)
    user_id = Column(Integer)
    item_id = Column(Integer)
    content = Column(String(256))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


@auto_rollback
def create_item_comment(content, item=None, user=None):
    now = datetime.now()
    item_comment = ItemComment(
        content=content,
        created_at=now,
        updated_at=now,
        item_id=item.id if item else None,
        user_id=user.id if user else None
    )
    session.add(item_comment)
    session.commit()


def find_user_item_comments(user_or_id, item_or_id):
    return session.query(ItemComment) \
        .filter_by(user_id=user_or_id if isinstance(user_or_id, int) else user_or_id.id,
                   item_id=item_or_id if isinstance(item_or_id, int) else item_or_id.id) \
        .order_by(ItemComment.created_at.desc()) \
        .all()


@auto_rollback
def delete_user_item_comment(user_or_id, item_or_id, comment_or_id):
    item_comment = session.query(ItemComment) \
        .filter_by(user_id=user_or_id if isinstance(user_or_id, int) else user_or_id.id,
                   item_id=item_or_id if isinstance(item_or_id, int) else item_or_id.id,
                   id=comment_or_id if isinstance(comment_or_id, int) else comment_or_id.id) \
        .first()
    if item_comment:
        session.delete(item_comment)
        session.commit()
        return True
