import os

from social_login.settings import BASE_DIR

SECRET_KEY = '_n8_1vxfksbwy0$vwqdc%^4_2kg0n0^jd0363i47i*$rhs0c4n'

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', '..', 'logs', 'debug.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

ALLOWED_HOSTS = ['127.0.0.1', 'fbapp.duckdns.org', 'fbapp.hopto.org', 'demo.rktcnepal.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'roshanshrestha01@gmail.com'
DEFAULT_FROM_EMAIL = 'roshanshrestha01@gmail.com'
SERVER_EMAIL = 'roshanshrestha01@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['GMAIL_PASSWORD']


ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
