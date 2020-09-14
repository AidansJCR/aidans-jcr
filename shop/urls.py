from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from search import views as search_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from django.contrib.auth import views as auth_views
from shop import views
from home import views as home_views


urlpatterns = [
    #The api url patterns
    path('login', home_views.login),
    path('logout', home_views.logout),
    
    path('setup', views.setup),
    path('setup/addingredient', views.add_ingredient),

    path('getingredients', views.get_ingredients),
    path('', views.home),
]
