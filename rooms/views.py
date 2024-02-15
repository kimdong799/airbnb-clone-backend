from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
# view : 유저가 특정 url에 접근했을 때 작동하는 함수


def see_all_rooms(request):
    return HttpResponse(Room.objects.all())


def see_one_room(request, room_id):
    return HttpResponse(Room.objects.get(pk=room_id))


def see_one_room_with_name(request, room_id, room_name):
    return HttpResponse(f"Room ID : {room_id} / {room_name}")
