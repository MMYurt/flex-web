# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request):
    return render(request, 'chat/room3.html', {
        #'room_name_json': mark_safe(json.dumps(room_name))
    })

def output(request):
    return render(request, 'chat/output.html', {})