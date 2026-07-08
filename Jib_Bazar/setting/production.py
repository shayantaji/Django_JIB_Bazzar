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
        'NAME': 'ssqhudjj_jibbazar_project_db',
        'USER': 'ssqhudjj_shayan11exe',
        'PASSWORD': 'Def11esteghlal',
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