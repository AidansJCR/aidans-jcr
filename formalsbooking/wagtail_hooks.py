from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import Booking, Event

class WagtailBookingAdmin(ModelAdmin):
    model = Booking
    menu_label = 'Bookings'
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

class WagtailFormalsAdminGroup(ModelAdminGroup):
    menu_label = 'Formals'
    menu_icon = 'tick'
    menu_order = 700
    items = (WagtailBookingAdmin, WagtailEventAdmin)

modeladmin_register(WagtailFormalsAdminGroup)
