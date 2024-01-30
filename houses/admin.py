from django.contrib import admin
from .models import House
# Register your models here.

# House 모델 Admin 패널 추가
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # admin 패널 컬럼 항목 추가
    list_display = (
        'name',
        'price_per_night',
        'address',
        'pets_allowed',
    )

    # 필터 항목 추가
    list_filter = (
        'price_per_night',
        'pets_allowed',
    )

    # 검색바 추가
    search_fields = (
        'address',
    ) # element가 하나인 경우 , 가 반드시 필요함 (튜플)