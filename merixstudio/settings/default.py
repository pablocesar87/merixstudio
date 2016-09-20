from os import path
from django.utils.translation import ugettext_lazy as _

dirname = path.dirname

BASE_DIR = dirname(dirname(dirname(path.abspath(__file__))))
DEBUG = True



ALLOWED_HOSTS = []

SECRET_SENTINEL = 'Elephant in Cairo'
SECRET_KEY = 'Elephant in Cairo'

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'compressor',
    # 'mailqueue',
    #'rosetta',
    # 'widget_tweaks',
    # 'stdimage',
    # 'sendfile',
    'haystack',
    'debug_toolbar',
    'merixstudio',
    'auth_ex',
    'blog',
    'articles',
    'comments'
)


# --- HAYSTACK---
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/gettingstarted'
    },
}


AUTH_USER_MODEL = 'auth_ex.User'
LOGIN_REDIRECT_URL = '/admin/'

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# --- MEDIA ---
MEDIA_URL = '/media/'
STATIC_MEDIA = path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['merixstudio/search_configuration'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ),
        }
    },
]

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
)

ROOT_URLCONF = 'merixstudio.urls'
WSGI_APPLICATION = 'merixstudio.wsgi.application'

USE_TZ = False
TIME_ZONE = 'UTC'

# --- LANGUAGES ---
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'
# LANGUAGES = (
#     ('en', _('English')),
#     ('pl', _('Polish')),
# )
# LOCALE_PATHS = (
#     path.join(BASE_DIR, 'locale'),
# )

# --- FILE UPLOAD ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# --- DATABASE ---
# --- POSTGRESQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '',
        'NAME': '',
        'PASSWORD': '',
        'PORT': '',
        'USER': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# --- DJANGO COMPRESSOR ---
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

# --- CACHE ---
# {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'TIMEOUT': 300,
#     }
# }

# --- DJANGO REGISTRATION REDUX ---
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1']

# --- SENTRY ---
# INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
# RAVEN_CONFIG = {
#     'dsn': '',
# }
# LOGGING['handlers']['sentry'] = {
#     'class': 'raven.handlers.logging.SentryHandler',
#     'level': 'WARNING',
# }
# LOGGING['loggers'][''] = {
#     'handlers': ['console', 'sentry'],
#     'level': 'DEBUG',
#     'propagate': False,
# }
# LOGGING['loggers']['merixstudio'] = {
#     'handlers': ['sentry'],
#     'level': 'INFO',
#     'propagate': True,
#     'formatter': 'simple',
# }
