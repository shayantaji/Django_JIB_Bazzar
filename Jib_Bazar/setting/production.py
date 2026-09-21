from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "jibbazar.ir",
    "www.jibbazar.ir",
]

CSRF_TRUSTED_ORIGINS = [
    "https://jibbazar.ir",
    "https://www.jibbazar.ir",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'OPTIONS': {
            'autocommit': True,
        }
    }
}


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = "/home/ssqhudjj/public_html/static"

MEDIA_ROOT = "/home/ssqhudjj/public_html/medias"