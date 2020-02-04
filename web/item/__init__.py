from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from db.item import create_item as _create_item, get_user_item_detail, delete_user_item, done_user_item, \
    reset_user_item_done

blueprint = Blueprint('item', __name__, url_prefix='/items')


@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('item/create.html')
    else:
        title = request.form.get('title')
        video_url = request.form.get('video_url')
        if title:
            _create_item(title, video_url, user=current_user)
        return redirect(url_for('main.index'))


@blueprint.route('/<int:item_id>', methods=['GET', 'DELETE'])
@login_required
def detail(item_id):
    item = get_user_item_detail(current_user, item_id)
    if not item:
        return 'not found', 404
    if request.method == 'GET':
        return render_template('item/detail.html', item=item)
    elif request.method == 'DELETE':
        delete_user_item(current_user, item_id)
        return 'ok'


@blueprint.route('/<int:item_id>/done', methods=['POST', 'DELETE'])
@login_required
def done(item_id):
    if request.method == 'POST':
        done_user_item(current_user, item_id)
        return 'ok'
    elif request.method == 'DELETE':
        reset_user_item_done(current_user, item_id)
        return 'ok'


from . import comment
