from django.contrib import admin
from .models import Event, Booking, Group

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class BookingAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Group, GroupAdmin)
