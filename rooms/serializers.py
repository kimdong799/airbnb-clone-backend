from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from wishlists.models import Wishlist
from .models import Amenity, Room
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()
    amenities = AmenitySerializer(
        many=True,
        read_only=True,
    )
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "amenities",
            "photos",
            "is_liked",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context.get("request")
        if request:
            return room.owner == request.user
        return False

    def get_is_liked(self, room):
        request = self.context.get("request")
        print(request)
        return Wishlist.objects.filter(
            user=request.user,
            rooms__id=room.pk,
        ).exists()


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    category = CategorySerializer(
        read_only=True,
    )
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()
    amenities = AmenitySerializer(
        many=True,
        read_only=True,
    )
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context.get("request")
        if request:
            return room.owner == request.user
        return False

    def get_is_liked(self, room):
        request = self.context.get("request")
        return Wishlist.objects.filter(
            user=request.user,
            rooms__id=room.pk,
        ).exists()
