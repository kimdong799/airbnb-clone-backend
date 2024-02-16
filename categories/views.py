from django.http import JsonResponse
from django.shortcuts import render
from .models import Category


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse({"ok": True})
