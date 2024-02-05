from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """Room and Experience Category"""

    def __str__(self):
        return f"{self.kind.title()}: {self.name}"

    class CategoryKindChoices(models.TextChoices):
        ROOM = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(
        max_length=150,
    )
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices,
    )

    class Meta:
        verbose_name_plural = "Categories"
