from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
        A form generated for the user to create an event booking.
    """
    class Meta:
        model = Booking
        fields = ['event', 'group', 'dietary_requirements', 'wine_choice']
