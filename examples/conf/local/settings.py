from examples.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

print PROJECT_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'dbs', 'ex1.db'),
    }
}

ROOT_URLCONF = '%s.conf.local.urls' % PROJECT_MODULE_NAME

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
