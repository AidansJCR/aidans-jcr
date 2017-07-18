from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from .models import Booking, Event

class WagtailBookingAdmin(ModelAdmin):
    model = Booking
    menu_label = 'Formals'
    menu_icon = 'tick'
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('user', 'group', 'event', 'dietary_requirements', 'wine_choice')
    search_fields = ('__all__',)

class WagtailEventAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'
    menu_order = 600
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'description', 'time',)
    search_fields = ('name',)

modeladmin_register(WagtailBookingAdmin)
modeladmin_register(WagtailEventAdmin)
