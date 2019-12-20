from __future__ import absolute_import, unicode_literals
from .base import *
import os
import environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y3nc$5+yz$j-z6*b391t196qli7$vs4yqux=spn_#4h+8a3%ec'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ENV_PATH = os.path.join(BASE_DIR, '.env.dev')

if os.path.isfile(ENV_PATH):
    env = environ.Env()
    environ.Env.read_env(ENV_PATH)

    # Load in some development database
    DATABASES['jcrdb'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('AWS_JCR_DATA_NAME'),
        'HOST': env('AWS_JCR_DATA_HOST'),
        'PORT': env('AWS_JCR_DATA_PORT'),
        'USER': env('AWS_JCR_DATA_USER'),
        'PASSWORD': env('AWS_JCR_DATA_PASS')
    }

else:
    print('Local .env file does not exist')

try:
    from .local import *
except ImportError:
    pass
