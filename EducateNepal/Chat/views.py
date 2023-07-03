import re
from django.shortcuts import render
from django.contrib.auth.models import User
def index(request):
    users=User.objects.exclude(pk=request.user.id).all()
    return render(request, 'chat/index.html', {'users':users})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })