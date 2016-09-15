# -*- coding: utf-8 -*-

import random
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

option = '['+bcolors.OKBLUE+'x'+bcolors.ENDC+']'
    
project_name = sys.argv[1:][0]
base_dir = sys.argv[1:][1]
dbname = sys.argv[1:][2]
install_mode = sys.argv[1:][3]
project_dir = base_dir+'/'+project_name

msg = 'What is the timezone of your project? [UTC] > '
timezone = raw_input(msg)
if not timezone:
    timezone = 'UTC'
print "Timezone set to "+timezone
    
msg = 'What is the language code for your project? [en] > '
language_code = raw_input(msg)
if not language_code:
    language_code = 'en'
print "Language code set to "+language_code

msg = 'Debug: [Y/n] > '
debug_msg = raw_input(msg)
debug = True
if debug_msg == 'n' or debug_msg == 'no':
    debug = False
    print "Debug mode is disabled"
else:
    print "Debug mode is enabled"

databases = {
            'sqlite':"""DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    }
                }""",
             }
database = databases['sqlite']

def secret_key():
    return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

file_content = """# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '"""+secret_key()+"""'

# SECURITY WARNING: don't run with debug turned on in production!\n\n"""
if debug is True:
    file_content += 'DEBUG = True\n'
else:
    file_content += 'DEBUG = False\n'
file_content += 'DEBUG_TOOLBAR = False\n'
    
file_content += """

ALLOWED_HOSTS = ['127.0.0.1','localhost']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'sysmon',
    'mbase',
    'mqueue',
    'bootstrap3',
    'bootstrapform',
    "mptt",
    "easy_thumbnails",
    "filer",
    # !extra_apps!
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '"""+project_name+""".urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = '"""+project_name+""".wsgi.application'

"""+database+"""

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'), )

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = '"""+language_code+"""'

TIME_ZONE = '"""+timezone+"""'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 1

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = "/account/logout/"

APPEND_SLASH = True

if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False

#~ debug
if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES+=('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS+=('debug_toolbar',)
    JQUERY_URL = '/static/js/jquery-2.1.4.min.js'
"""

# generate settings
filepath=project_dir+'/'+project_name+'/settings.py'
filex = open(filepath, "w")
filex.write(file_content)
filex.close()

