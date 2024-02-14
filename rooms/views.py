from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view : 유저가 특정 url에 접근했을 때 작동하는 함수


def say_hello(request):
    return HttpResponse(f"Hello {request.user}!")
