from django.shortcuts import render
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.db.utils import IntegrityError
import json
from .models import Group
# Create your views here.

def api_add_group(request):
    resp = {}
    if not request.user.is_authenticated:
        # return a JSON error
        resp['error'] = 'User not authenticated'
    else:
        new_group = Group.objects.create()
        resp['group_id'] = new_group.pk
    return HttpResponse(json.dumps(resp), content_type="text/json")


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
            # todo check whether group has been entered, otherwise specify a new group.
            booking.group = Group.objects.get(pk=request.group_id)
            # now save the booking, rendering an error if one occurs.
            try:
                booking.save()

                # Now send a confirmation email to the booking party.
                email_subject = "Booking for " + str(form.event) + " complete."

                email_message = "Thank you, your booking for " + str(booking.event) + "is now complete. \n"
                email_message += "Please keep an eye on your emails, as confirmation will be sent soon regarding whether"
                email_message += " you have been successful. \n\n"
                email_message += "Thank you for booking with Aidan's JCR"
                email_to = [request.user.email]

                send_mail(email_subject, email_message, "no-reply@st-aidans.com", email_to)
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
