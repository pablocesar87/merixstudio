SITE_ID=1

#You can create an user for the database of change DB configuration to trusted
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'YOUR_HOST',
        'NAME': 'YOUR_DATABASE_PROJECT_NAME',
        'PASSWORD': 'YOUR_DB_PASS',
        'PORT': '',
        'USER': 'YOUR_DB_USER',
    }
}

TIME_ZONE = 'UTC'
#Set to your own time zone



# CELERY SETTINGS---- Use your own celery settings
BROKER_URL = ''
CELERY_ACCEPT_CONTENT = []
CELERY_TASK_SERIALIZER = ''
CELERY_RESULT_SERIALIZER = ''

'''
After change your settings, rename this file to local.py
'''