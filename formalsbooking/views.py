from django.shortcuts import render
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.db.utils import IntegrityError
# Create your views here.


@login_required
def new_booking(request):
    """ Create a new event booking """
    if(request.method == 'POST'):
        # we submit the form through a POST request
        form = BookingForm(request.POST)
        if form.is_valid():
            # If the form data is itself valid, add the user data to the form.
            # then submit it.
            booking = form.save(commit=False)
            booking.user = request.user

            # now save the booking, rendering an error if one occurs.
            try:
                booking.save()
            except IntegrityError as e1:
                ERROR_MESSAGE = "You already have a booking for this event."
                return render(request, 'formalsbooking/new_booking.html', {'form': form, 'error': ERROR_MESSAGE })
            except Exception as e2:
                return render(request, 'formalsbooking/new_booking.html', {'form': form, 'error': e2 })
        else:
            return render(request, 'formalsbooking/new_booking.html', {'form': form, 'error': "The form is invalid. Please ensure all required fields are filled in." })

    # Otherwise, show the user a new form.
    form = BookingForm()
    return render(request, 'formalsbooking/new_booking.html', {'form': form})
