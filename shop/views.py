from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
import json
import requests

# Create your views here.
@login_required(login_url='/user/login')
def home(request):
    return render(request, 'home.html')#, {'items':items})


def setup(request):
    return render(request, 'setup.html')

    #if request.method == 'POST':
        #Grab data from post request
        #Return success
