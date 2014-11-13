"""
Django settings for koieadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from os.path import dirname, realpath, join
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ge_q)l68gr3%sb6u)*1kb*yc&h4-4_e8xg7^7ax*+8i(qcllu9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'k.sklirg.io']



ADMINS = (('Sklirg', 'sklirg@sklirg.io'),)

ADMINS = (('Sklirg', 'sklirg@sklirg.io'),)

BASE_URL = 'http://k.sklirg.io'

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'widget_tweaks',
    'koie',
    'django_extensions',
    'djcelery',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ROOT_URLCONF = 'koieadmin.urls'

WSGI_APPLICATION = 'koieadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.db'),
    }
}"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'it1901',
        'USER': 'it1901',
        'PASSWORD': 'X9K9DLqNJyGzGw7zFpR5',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', 'English'),
    ('nb', 'Norsk bokmål'),
)

LANGUAGE_CODE = 'nb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.ERROR: 'danger',}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = join(PROJECT_ROOT, 'static/')

import djcelery
djcelery.setup_loader()

BROKER_URL = 'amqp://guest:guest@localhost:5672'

# Setup for email using gmail as a SMTP host

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ntnu.koier@gmail.com'
EMAIL_HOST_PASSWORD = 'it1901it1901'
