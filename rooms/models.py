from django.db import models
from common.models import CommonModel  # 공통 Model 로직


# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=180,
        default="",
    )
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
        # user_set 명칭 변경
        related_name="rooms",
    )
    # N : M 관계 지정
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        # user_set 명칭 변경
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        # user_set 명칭 변경
        related_name="rooms",
    )

    def __str__(self):
        return self.name

    def total_amenities(self):
        print(self)
        return self.amenities.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            # values로 접근해야 모든 속성에 접근하지 않아 최적화 가능
            return round(
                sum(
                    [review["rating"] for review in self.reviews.all().values("rating")]
                )
                / self.reviews.count(),
                2,
            )


class Amenity(CommonModel):
    """Amenity Definitnion"""

    def __str__(self):
        return self.name

    class Meta:
        # admin 패널에 표시되는 Amenitys 오타 수정 (직접 지정)
        verbose_name_plural = "Amenities"

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        # django db에서 null가능
        null=True,
        # form에서 빈 값 가능
        blank=True,
    )
