from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DATABASES = {
    'default': {
        'ENGINE': get_secret("LOCAL_DATABASE_ENGINE"),
        'NAME': 'wolverine_den',
        'USER': get_secret("LOCAL_DATABASE_USER"),
        'PASSWORD': get_secret("LOCAL_DATABASE_PASSWORD"),
        'HOST': get_secret("LOCAL_DATABASE_HOST"),
        'PORT': get_secret("LOCAL_DATABASE_PORT"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}