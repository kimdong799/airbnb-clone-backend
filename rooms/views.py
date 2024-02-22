from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework import status
from .models import Room, Amenity
from categories.models import Category
from .serializers import RoomDetailSerializer, RoomListSerializer, AmenitySerializer

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
        serializer = RoomDetailSerializer(self.get_object(pk))
        return Response(serializer.data)

    def post(self, request, pk):
        # user 인증
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                # user request의 category 전달
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError
                except Category.DoesNotExist:
                    raise ParseError

                # owner는 request를 보낸 user로 지정
                # create 메소드의 validated_data에 추가
                room = serializer.save(
                    owner=request.user,
                    category=category,
                )
                serializer = RoomDetailSerializer(room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated
