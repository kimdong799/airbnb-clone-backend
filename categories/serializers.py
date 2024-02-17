from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # 노출하고자 하는 필드 정의
    pk = serializers.IntegerField(
        read_only=True,
    )
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=15,
    )
    created_at = serializers.DateTimeField(
        read_only=True,
    )
