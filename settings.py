import os

env = os.environ.get

DEBUG = env('DEBUG')

SECRET_KEY = 'thequickbrownfoxjumpsoverthelazydog'

SQLALCHEMY_URI = env('SQLALCHEMY_URI', 'sqlite:///todolist.db')

# https://getbootstrap.com/
CDN_JQUERY_JS = env(
    'CDN_JQUERY_JS',
    '<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>'
)
CDN_POPPER_JS = env(
    'CDN_POPPER_JS',
    '<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>'
)
CDN_BOOTSTRAP_JS = env(
    'CDN_BOOTSTRAP_JS',
    '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>'
)
CDN_BOOTSTRAP_CSS = env(
    'CDN_BOOTSTRAP_CSS',
    '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
)

# https://cn.vuejs.org/v2/guide/
CDN_VUE_JS = env(
    'CDN_VUE_JS', '<script src="https://cdn.jsdelivr.net/npm/vue"></script>'
)
