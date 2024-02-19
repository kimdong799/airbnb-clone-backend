from django.urls import path
from . import views


urlpatterns = [
    # path("", views.categories),
    # path("<int:pk>", views.category),
    path("", views.Categories.as_view()),  # APIView 사용 시
    path("<int:pk>", views.CategoryDetail.as_view()),
]
