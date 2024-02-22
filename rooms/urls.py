from django.urls import path
from . import views
from .models import Room, Amenity

urlpatterns = [
    path("", views.Rooms.as_view()),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),
]
