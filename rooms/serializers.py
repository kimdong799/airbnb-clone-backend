from rest_framework import serializers
from .models import Room, Amenity


# ModelSerializer를 사용하면 id, created_at, updated_at 필드는 자동으로 read_only로 지정됨
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        # Serilizer Relationship 추가 (가장 쉬운 방법)
        # 커스터마이징 불가 단점
        depth = 1


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
