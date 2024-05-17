from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("log-in", views.Login.as_view()),  # Cookie Login
    path("token-login", obtain_auth_token),  # Token Login
    path("jwt-login", views.JWTLogin.as_view()),  # JWT Login
    path("github", views.GithubLogin.as_view()),  # GitHub Login
    path("log-out", views.Logout.as_view()),
    # me 라는 이름의 user 검색을 방지
    path("@<str:username>", views.PublicUser.as_view()),
    path("@<str:username>/rooms", views.UserRooms.as_view()),
    path("@<str:username>/reviews", views.UserReviews.as_view()),
    path("change-password", views.ChangePassword.as_view()),
]
