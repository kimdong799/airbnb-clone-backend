from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view()
def categories(request):
    all_categories = Category.objects.all()
    # 다수의 객체 정보를 직렬화 하기 위해 many 인자 전달
    serializer = CategorySerializer(all_categories, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
