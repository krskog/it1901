"""
Django settings for koieadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from os.path import dirname, realpath, join
PROJECT_ROOT = BASE_DIR

PROJECT_SETTINGS_DIRECTORY = os.path.dirname(globals()['__file__'])


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

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

# Broker URL is set in local.py

# Remember to keep 'local' last, so it can override any setting.
for settings_module in ['local']:  # local last
    if not os.path.exists(os.path.join(PROJECT_SETTINGS_DIRECTORY,
            settings_module + ".py")):
        sys.stderr.write("Could not find settings module '%s'.\n" %
                settings_module)
        if settings_module == 'local':
            sys.stderr.write("You need to copy the settings file "
                             "'koieadmin/settings/example-local.py' to "
                             "'koieadmin/settings/local.py'.\n")
        sys.exit(1)
    try:
        exec('from %s import *' % settings_module)
    except ImportError:
        print("Could not import settings for '%s'" % settings_module)
