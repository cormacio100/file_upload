from base import *
import dj_database_url


DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

ALLOWED_HOSTS.append('file-upload-cormac.herokuapp.com')

LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'handlers':{
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers':{
        'django':{
            'handlers':['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL','DEBUG'),
        },
    },
}
