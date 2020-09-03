from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from search import views as search_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from django.contrib.auth import views as auth_views
from home import views as home_views

urlpatterns = [
    #path('api/', include('home.api_urls')),
    #path('user/', include('home.urls')),
    #path('shop/', include('shop.urls')),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^django-admin/', admin.site.urls),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^search/$', search_views.search, name='search'),
    re_path(r'^sitemap\.xml$', sitemap),
    re_path(r'', include(wagtail_urls)),
]



from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Serve static and media files from development server
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
