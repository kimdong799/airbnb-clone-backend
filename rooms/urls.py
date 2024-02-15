from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    # url로부터 받을 parameter 데이터 타입 명시
    path("<int:room_id>", views.see_one_room),
    # 복수의 parameter를 받는 경우
    path("<int:room_id>/<str:room_name>", views.see_one_room_with_name),
]
