from django.contrib import admin
from .models import ChattingRoom, Messages


@admin.register(ChattingRoom)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at",)


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "user",
        "ChattingRoom",
        "created_at",
    )
    list_filter = ("created_at",)
