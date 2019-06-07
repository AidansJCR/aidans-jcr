from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from home.models import AppAnnouncement
import datetime


@login_required(login_url='/app/login')
def app_home_page(request):
    return render(request, 'home/app/home_page.html')


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


@login_required(login_url='/app/login')
def app_announcements(request):
    if request.method == 'POST':
        if request.POST['function'] == 'upload':
            #If the user is uploading an announcement
            announcement = AppAnnouncement(title=request.POST['title'], message=request.POST['message'], image=request.FILES['image'], time_set=datetime.datetime.now())
            announcement.save()
        elif request.POST['function'] == 'delete':
            #If the user is removing an announcement
            AppAnnouncement.objects.get(pk=request.POST['announcementId']).delete()
        return redirect('/app/announcements')
    elif request.method == 'GET':
        announcements = AppAnnouncement.objects.all()
        return render(request, 'home/app/announcements.html', {'announcements':announcements})
    return null


def app_get_announcements(request):
    #Send back the announcements in a json format
    announcements = list(AppAnnouncement.objects.all().values())
    return JsonResponse(announcements, safe=False)


@login_required(login_url='/app/login')
def app_schedule(request):
    if request.method == 'POST':
        if request.POST['function'] == 'upload':
            #If the user is uploading an announcement
            announcement = AppAnnouncement(title=request.POST['title'], message=request.POST['message'], image=request.FILES['image'], time_set=datetime.datetime.now())
            announcement.save()
        elif request.POST['function'] == 'delete':
            #If the user is removing an announcement
            AppAnnouncement.objects.get(pk=request.POST['announcementId']).delete()
        return redirect('home/app/announcements')
    elif request.method == 'GET':
        announcements = AppAnnouncement.objects.all()
        return render(request, 'home/app/announcements.html', {'announcements':announcements})
    return null
