from django import forms
from .models import Booking

# Django Admin Stuff
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
