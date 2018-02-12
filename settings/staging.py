from base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS.append('file-upload-cormac-s3.herokuapp.com')

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}