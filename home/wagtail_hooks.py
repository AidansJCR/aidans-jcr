from django.urls import reverse

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

@hooks.register('register_admin_menu_item')
def register_menu_item():
  return MenuItem('App Content', "app", classnames='icon icon-folder-inverse', order=200)
