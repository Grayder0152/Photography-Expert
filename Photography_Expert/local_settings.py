import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-j=ri%2mtyz-isic%23e!#gi-hg*rje*3v+%dy#sxo-si+%3n@'

DEBUG = True


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [STATIC_DIR]