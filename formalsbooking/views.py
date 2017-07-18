from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def new_booking(request):
    form = BookingForm()
    return render(request, 'formalsbooking/new_booking.html', {'form': form})
