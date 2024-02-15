from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
# view : 유저가 특정 url에 접근했을 때 작동하는 함수


def see_all_rooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "Hello! this title comes from django",
        },
    )


def see_one_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )


def see_one_room_with_name(request, room_id, room_name):
    return HttpResponse(f"Room ID : {room_id} / {room_name}")
