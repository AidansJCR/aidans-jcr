from django.contrib import admin
from .models import Event, Booking

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
