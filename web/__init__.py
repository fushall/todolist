from importlib import import_module
from pprint import pprint

from flask import Flask
from flask_login import LoginManager
from werkzeug.utils import find_modules

from db import init_db
from db.user import get_user

# database
init_db()

# flask app and flask exts
app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'main.login'
login_manager.user_loader(lambda user_id: get_user(user_id))

# flask config
app.config.from_pyfile('../settings.py')

# auto-import blueprint
for module_path in find_modules(__name__, include_packages=True):
    module = import_module(module_path)
    blueprint = getattr(module, 'blueprint', None)
    if blueprint:
        app.register_blueprint(blueprint)

pprint(app.url_map)
pprint(app.config)
