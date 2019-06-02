from django.http import Http404
from django.shortcuts import render

def app_view(request):
    return render(request, 'home/app_page.html')
