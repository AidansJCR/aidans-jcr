from .models import Album
from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
# Register your models here

class AlbumModelAdmin(ModelAdmin):
    model = Album
    menu_label = "Albums"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('collection','description',)


# Use the Wagtail Model Admin.

modeladmin_register(AlbumModelAdmin)
