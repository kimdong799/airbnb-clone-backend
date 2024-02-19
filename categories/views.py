from django.shortcuts import render
from rest_framework.exceptions import NotFound  # 404 Error
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        # 다수의 객체 정보를 직렬화 하기 위해 many 인자 전달
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # POST 데이터를 시리얼라이저에 전달
        serializer = CategorySerializer(data=request.data)
        # User Input 검증
        print(serializer.is_valid())
        if serializer.is_valid():
            # save() 호출 시 serializer의 create()가 호출된
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorySerializer(
            category,
            many=False,
        )
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            # 일부 데이터만 변경 가능
            partial=True,
            many=False,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
