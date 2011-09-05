from South Sanity Demos.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'South Sanity Demos.conf.dev.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'South Sanity Demos',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
