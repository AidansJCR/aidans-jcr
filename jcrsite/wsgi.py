"""
WSGI config for jcrsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jcrsite.settings.production")

application = get_wsgi_application()
application = WhiteNoise(application)
