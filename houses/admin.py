from django.contrib import admin
from .models import House
# Register your models here.

# House 모델 Admin 패널 추가
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass