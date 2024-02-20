from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User
from config import settings
import os


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "avatar_thumbnail",
        "username",
        "email",
        "name",
        "is_host",
        "hosting_rooms",
    )
    list_display_links = (
        "avatar_thumbnail",
        "username",
        "email",
    )

    def avatar_thumbnail(self, obj):
        if obj.avatar:
            print(obj.avatar.url)
            return format_html(
                '<img src="{}" style="border-radius: 50%; max-width: 50px; max-height: 50px;" />'.format(
                    obj.avatar.url
                )
            )
        else:
            return format_html(
                '<img src="{}" style="border-radius: 50%; max-width: 50px; max-height: 50px;" />'.format(
                    os.path.join(settings.MEDIA_URL, "avatars/default_profile.jpeg")
                )
            )

    avatar_thumbnail.short_description = "Avatar"
