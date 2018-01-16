from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from .views import finance_home

urlpatterns = [
    url(r'^finance/$', finance_home, name='finance'),
]
