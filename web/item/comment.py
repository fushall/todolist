from flask import request
from flask_login import login_required, current_user

from db.item import find_user_item
from db.item_comment import find_user_item_comments, create_item_comment, delete_user_item_comment
from . import blueprint


def get_user_item_comments(item):
    item_comments = find_user_item_comments(current_user, item.id)
    return {
        'comments': [
            {
                'id': comment.id,
                'content': comment.content,
                'created_at': comment.created_at.timestamp(),
                'updated_at': comment.updated_at.timestamp(),
            } for comment in item_comments
        ]
    }


@blueprint.route('/<int:item_id>/comments')
@login_required
def comments(item_id):
    item = find_user_item(current_user, item_id)
    if not item:
        return 'not found the item', 404

    return get_user_item_comments(item)


@blueprint.route('/<int:item_id>/comments', methods=['POST'])
@login_required
def create_comment(item_id):
    item = find_user_item(current_user, item_id)
    if not item:
        return 'not found the item', 404

    content = request.json.get('content')
    create_item_comment(content, item=item, user=current_user)
    return 'ok'


@blueprint.route('/<int:item_id>/comments/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(item_id, comment_id):
    item = find_user_item(current_user, item_id)
    if not item:
        return 'not found the item', 404

    delete_user_item_comment(current_user, item_id, comment_id)
    return get_user_item_comments(item)
