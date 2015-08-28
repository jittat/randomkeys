from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json

from models import Room, Keyword

def index(request, room_title):
    room, is_created = Room.objects.get_or_create(title=room_title)

    context = {'room': room}
    
    return render(request,
                  'topics/index.html',
                  context)


def list(request, room_title):
    room = get_object_or_404(Room, title=room_title)
    keywords = room.keyword_set.all()

    names = [k.name for k in keywords]
    print names
    json_data = json.dumps(names)
    
    return HttpResponse(json_data, content_type='application/json')


def add_keyword(request, room_title):
    room = get_object_or_404(Room, title=room_title)

    keyword_str = request.POST['keyword'].strip()
    keywords = room.keyword_set.filter(name=keyword_str).all()
    if len(keywords)==0:
        keyword = Keyword(name=keyword_str, room=room)
        keyword.save()
    return HttpResponse('OK')

