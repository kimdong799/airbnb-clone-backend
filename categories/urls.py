from django.urls import path
from . import views


urlpatterns = [
    # path("", views.categories),
    # path("<int:pk>", views.category),
    #
    # APIView 사용 시
    # path("", views.Categories.as_view()),
    # path("<int:pk>", views.CategoryDetail.as_view()),
    #
    # ModelViewSet 사용 시
    path(
        "",
        views.CategoriyViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    # retrieve method는 pk를 받도록 되어있으니 주의
    path(
        "<int:pk>",
        views.CategoriyViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
