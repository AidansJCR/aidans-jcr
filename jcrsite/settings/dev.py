from __future__ import absolute_import, unicode_literals

from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y3nc$5+yz$j-z6*b391t196qli7$vs4yqux=spn_#4h+8a3%ec'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
