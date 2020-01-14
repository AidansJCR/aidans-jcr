from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connections
from django.contrib.auth.models import User

from home.models import AppAnnouncement, Event
from datetime import datetime
import json
import requests


@login_required(login_url='/user/login')
def home_page(request):
    return render(request, 'home/user/home.html')


def login(request):
    username = request.POST['username']

    if username in request.session:
        return redirect('/user')
    else:
        if request.method == 'GET':
            #They are requesting the login page
            return render(request, 'home/user/login.html', {'error':''})
        elif request.method == 'POST':
            password = request.POST['password']
            if requests.get('https://www.dur.ac.uk/its/password/validator', auth=(username,password)).status_code != 401:
                request.session['username'] == username.lower()
                return redirect('/user')
            else:
                return render(request, 'home/user/login.html', {'error':'Incorrect login'})
        #They are trying to do something weird
        return None


def logout(request):
    request.session.flush()
    return redirect('/user/login')


@login_required(login_url='/user/login')
def announcements(request):
    if request.method == 'POST':
        if request.POST['function'] == 'upload':
            #If the user is uploading an announcement
            announcement = AppAnnouncement(title=request.POST['title'], message=request.POST['message'], image=request.FILES['image'], time_set=datetime.datetime.now())
            announcement.save()
        elif request.POST['function'] == 'delete':
            #If the user is removing an announcement
            AppAnnouncement.objects.get(pk=request.POST['announcementId']).delete()
        return redirect('/user/announcements')
    elif request.method == 'GET':
        announcements = AppAnnouncement.objects.all()
        return render(request, 'home/user/announcements.html', {'announcements':announcements})
    return None


def get_announcements(request):
    if request.method == 'GET':
        #Send back the announcements in a json format
        announcements = list(AppAnnouncement.objects.order_by('time_set').values())
        return JsonResponse(announcements, safe=False)


@login_required(login_url='/user/login')
def schedule(request):
    if request.method == 'POST':
        if request.POST['function'] == 'upload':
            #If the user is uploading an announcement
            event = AppEvent(title=request.POST['title'], location=request.POST['location'], start_time=request.POST['start_time'], description=request.POST['description'])
            event.save()
        elif request.POST['function'] == 'delete':
            #If the user is removing an announcement
            AppEvent.objects.get(pk=request.POST['eventId']).delete()
        return redirect('home/user/schedule')
    elif request.method == 'GET':
        events = AppEvent.objects.all()
        return render(request, 'home/user/schedule.html', {'events':events})
    return None


def get_schedule(request):
    if request.method == 'GET':
        events = list(AppEvent.objects.order_by('start_time').values())
        return JsonResponse(events, safe=False)


def get_events(request):
    if request.method == 'GET':
        with connections['jcrdb'].cursor() as cursor:
            cursor.execute("SELECT * FROM events WHERE endtime <= NOW()::timestamp;")
            result = cursor.fetchall()
            response = []
            for row in result:
                reponse.append({'eventId':row[0],'title':row[1],'description':row[2],'startTime':row[3],'endTime':row[4],'location':row[5],
                'cost':row[6],'imageUrl':row[7]})
            return JsonResponse(response, safe=False)
    return None


# Really have to focus on security for this part to ensure people can't view each others messages
# I'd rather it didn't work at all...
def get_chat_msgs(request):
    if request.method == "GET":
        with connections['jcrdb'].cursor() as cursor:
            cursor.execute("SELECT * FROM messages WHERE convid ==%s;", [request.GET['convid']])
            result = cursor.fetchall()
            response = []
            for row in result:
                reponse.append({'sender':row[0],'timesent':row[1],'message':row[2]})
            return JsonResponse(response, safe=False)
