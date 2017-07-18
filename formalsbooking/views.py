from django.shortcuts import render
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
# Create your views here.


@login_required
def new_booking(request):

    if(request.method == 'POST'):
        # we submit the form
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
    form = BookingForm()
    return render(request, 'formalsbooking/new_booking.html', {'form': form})
