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
    path('login', home_views.login),
    path('logout', home_views.logout),
    path('announcements', home_views.announcements),
    path('getannouncements', home_views.get_announcements),
    path('schedule', home_views.schedule),
    path('getschedule', home_views.get_schedule),
    path('chat', home_views.schedule),
    path('booking', home_views.schedule),
    path('', home_views.home_page),
]



from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Serve static and media files from development server
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
