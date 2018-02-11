from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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
