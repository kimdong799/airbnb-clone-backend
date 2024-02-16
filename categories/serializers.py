from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # 노출하고자 하는 필드 정의
    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
