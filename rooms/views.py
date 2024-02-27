from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework import status
from .models import Room, Amenity
from categories.models import Category
from .serializers import RoomDetailSerializer, RoomListSerializer, AmenitySerializer
from reviews.serializers import ReviewSerializer

# Create your views here.
# view : 유저가 특정 url에 접근했을 때 작동하는 함수


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(
            all_amenities,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound
        return amenity

    def get(self, request, pk):
        serializer = AmenitySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = AmenitySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Serializer Relationship
class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serialzer = RoomListSerializer(
            all_rooms,
            many=True,
            context={"request": request},
        )
        return Response(serialzer.data)


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
        return room

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(
            room,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request, pk):
        # user 인증
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                # user request의 category 전달
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required.")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The Category kind should be rooms")
                except Category.DoesNotExist:
                    raise ParseError("Category not found")

                # owner는 request를 보낸 user로 지정
                # create 메소드의 validated_data에 추가
                # transaction.atomic()을 이용하여 Query 실패 시 DB 롤백
                try:
                    with transaction.atomic():
                        room = serializer.save(
                            owner=request.user,
                            category=category,
                        )
                        # ManyToMany Field를 room object에 전달
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated

    def put(self, request, pk):
        room = self.get_object(pk)
        # room의 주인이 아니라면 방을 수정할 수 없도록 코딩
        # 로그인되어있는지 확인
        # 두 로직 모두 동작하도록 설계
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        serializer = RoomDetailSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            category_pk = request.data.get("category")
            # category 입력값이 존재하는 경우 validation 로직 수행
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                except Exception:
                    raise ParseError("The Category kind should be rooms")
            try:
                with transaction.atomic():
                    # User는 변경하지 않음
                    if category_pk:
                        room = serializer.save(
                            category=category,
                        )
                    # amenities 입력값 존재 시 수정
                    amenities = request.data.get("amenities")
                    if amenities:
                        # 기존의 amenities 제거
                        room.amenities.clear()
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    serializer = RoomDetailSerializer(
                        room,
                    )
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Amenity Not found")
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        # room의 주인이 아니라면 방을 삭제할 수 없도록 코딩
        # 로그인되어있는지 확인
        # 두 로직 모두 동작하도록 설계
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=status.HTTP_200_OK)


class RoomReviews(APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
        return room

    def get(self, request, pk):
        # 페지네이션을 위한 query_params 사용
        # page값이 존재하지 않는 경우 1로 지정
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            # 잘못된 page url요청 시 1로 지정
            page = 1
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializer = ReviewSerializer(
            room.reviews.all()[start:end],
            many=True,
        )
        return Response(serializer.data)


class RoomAmenities(APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
        return room

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size
        room = self.get_object(pk)
        serializer = AmenitySerializer(
            room.amenities.all()[start:end],
            many=True,
        )
        return Response(serializer.data)
