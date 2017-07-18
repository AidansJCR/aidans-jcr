from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'book/$', views.new_booking, name='new_booking'),
    url(r'api/add_group/$', views.api_add_group, name='add_group'),
]
