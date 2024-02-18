from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    # 노출하고자 하는 필드 정의
    pk = serializers.IntegerField(
        read_only=True,
    )
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(
        read_only=True,
    )

    def create(self, validated_data):
        # ** 는 input dict를 create 가능한 형태로 자동으로 변환해줌
        # name = validated_data.name ...
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
