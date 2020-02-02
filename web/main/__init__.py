from datetime import timedelta

from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

from db.item import find_user_undone_items, find_user_done_items
from db.user import User, session, create_user

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
@login_required
def index():
    checked_items = find_user_done_items(current_user)
    unchecked_items = find_user_undone_items(current_user)
    return render_template('main/index.html', checked_items=checked_items, unchecked_items=unchecked_items)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('main/register.html')
    else:
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        password_prompt = request.form.get('password_prompt', '')
        create_user(username=username, password=password, password_prompt=password_prompt)
        return redirect(url_for('main.index'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('main/login.html')
    else:
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        user = session.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user, duration=timedelta(minutes=5))
        return redirect(url_for('main.index'))


@blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.login'))
