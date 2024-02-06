from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """Wishlist Model Definition"""

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.room",
    )
    experiences = models.ManyToManyField(
        "experiences.experience",
    )
    user = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
