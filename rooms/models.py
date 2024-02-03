from django.db import models
from common.models import CommonModel  # 공통 Model 로직


# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    # Users앱 user모델과 관계지정
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    # N : M 관계 지정
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )


class Amenity(CommonModel):
    """Amenity Definitnion"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=50,
        null=True,
    )
