from django.contrib import admin
from .models import Room, Amenity


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "rooms",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    # default = __contains
    search_fields = (
        # ^ => startswith
        # = => equal
        "name",
        "^price",
        # FK 검색
        "owner__username",
    )
    # 수정 페이지에서 보고 싶은 경우 사용
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    # 수정 페이지에서 보고 싶은 경우 사용
    readonly_fields = (
        "created_at",
        "updated_at",
    )
