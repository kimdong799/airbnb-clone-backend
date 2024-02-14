from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"
    parameter_name = "word"

    def lookups(self, request, ModelAdmin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class RatingGradeFilter(admin.SimpleListFilter):
    title = "Filter by Rating grade"
    parameter_name = "rating_grade"

    def lookups(self, request, ModelAdmin):
        return [
            ("positive", "Positive"),
            ("negative", "Negative"),
        ]

    def queryset(self, request, reviews):
        if self.value() == "positive":
            return reviews.filter(rating__gte=3)
        elif self.value() == "negative":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        RatingGradeFilter,
        "rating",
        # FK 이용 필터링
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
