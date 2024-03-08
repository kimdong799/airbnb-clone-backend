from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    # me 라는 이름의 user 검색을 방지
    path("@<str:username>", views.PublicUser.as_view()),
    path("@<str:username>/rooms", views.UserRooms.as_view()),
    path("@<str:username>/reviews", views.UserReviews.as_view()),
    path("change-password", views.ChangePassword.as_view()),
]
