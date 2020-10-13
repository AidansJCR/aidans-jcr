from django.shortcuts import render

def index(request):
    return render(request, 'welfarechat/index.html', {})

def room(request, room_name):
    return render(request, 'welfarechat/room.html', {
        'room_name': room_name
    })
