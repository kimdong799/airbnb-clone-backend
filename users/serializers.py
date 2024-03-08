from rest_framework.serializers import SerializerMethodField, ModelSerializer
from .models import User as User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "avatar",
            "name",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )


class PublicUserSerializer(ModelSerializer):
    rooms = SerializerMethodField()
    reviews = SerializerMethodField()

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "last_login",
            "date_joined",
        )

    def get_rooms(self, user):
        return user.rooms.count()

    def get_reviews(self, user):
        return user.reviews.count()
