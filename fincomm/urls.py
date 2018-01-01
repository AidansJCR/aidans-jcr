from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from fincomm.views import display_transaction_list
urlpatterns = [
    url(r'^login/$', display_transaction_list),
]
