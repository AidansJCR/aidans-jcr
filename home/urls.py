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
from home import views as home_views

urlpatterns = [
    #The api url patterns
    path('login', home_views.app_login),
    path('logout', home_views.app_logout),
    path('announcements', home_views.app_announcements),
    path('getannouncements', home_views.app_get_announcements),
    path('schedule', home_views.app_schedule),
    path('getschedule', home_views.app_get_schedule),
    path('api/getEvents', home_views.get_events),
    path('', home_views.app_home_page),
]



from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Serve static and media files from development server
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
