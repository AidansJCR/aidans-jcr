from __future__ import absolute_import, unicode_literals

from .base import *
import dj_database_url
import os


db_from_env = dj_database_url.config(conn_max_age=500)
if db_from_env:
    DATABASES['default'].update(db_from_env)
    # AWS
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_S3_BUCKET_AUTH = False

    AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 4  # 4 hours
    AWS_QUERYSTRING_AUTH = False
    AWS_HEADERS = {
        'Cache-Control': 'max-age=86400',
    }

    # SendGrid
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    DEBUG = False

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    # SSL
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Static file compression and caching
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Load in the JCR DATABASE
    DATABASES['jcrdb'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['AWS_JCR_DATA_NAME'],
        'HOST': os.environ['AWS_JCR_DATA_HOST'],
        'PORT': os.environ['AWS_JCR_DATA_PORT'],
        'USER': os.environ['AWS_JCR_DATA_USER'],
        'PASSWORD': os.environ['AWS_JCR_DATA_PASS']
    }

try:
    from .local import *
except ImportError:
    pass
