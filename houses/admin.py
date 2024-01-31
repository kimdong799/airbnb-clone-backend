from django.contrib import admin
from .models import House

# Register your models here.


# House 모델 Admin 패널 추가
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # admin 패널 컬럼 항목 추가
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )

    # 필터 항목 추가
    list_filter = (
        "price_per_night",
        "pets_allowed",
    )
