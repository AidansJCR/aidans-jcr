from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from home.models import AppAnnouncement
import datetime


@login_required(login_url='/app/login')
def app_home_page(request):
    return render(request, 'home/app/home_page.html')


@login_required(login_url='/app/login')
def app_announcements_page(request):
    announcements = AppAnnouncement.objects.all()
    return render(request, 'home/app/announcements.html', {'announcements':announcements})


@login_required(login_url='/app/login')
def app_schedule_page(request):
    return render(request, 'home/app/schedule.html')


def app_login(request):
    if request.method == 'GET':
        #They are requesting the login page
        return render(request, 'home/app/login.html')
    elif request.method == 'POST':
        #They are sending us some data to try and login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app')
        else:
            return null
    else:
        #They are trying to do something weird
        return null


def app_logout(request):
    logout(request)
    return redirect('/app/login')


def app_announcements(request):
    if request.method == 'GET':
        #Return all of the announcements (should probably limit this to 24hrs at some point)
        return AppAnnouncement.objects.all()
    elif request.method == 'POST':
        p = AppAnnouncement(title=request.POST['title'], message=request.POST['message'], image=request.POST['image'], time_set=datetime.datetime.now())
        p.save()
        announcements = [p]
        return redirect('home/app/announcements.html', {'announcements':announcements})
