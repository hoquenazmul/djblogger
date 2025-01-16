import os
from .common import *  # noqa: F403


DEBUG = os.getenv('DEBUG')

SECRET_KEY = os.getenv('SECRET_KEY')

# TODO: Needs to be updated with prod domain/url
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    },
}