from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post
from .serializers import PostModelSerializer
# Create your views here.

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


def calculator(request):
    #1. 데이터 확인
    num1 = request.GET.get('num1',0)
    num2 = request.GET.get('num2',0)
    operators = request.GET.get('operators')

    #2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    if operators == '*':
        result = int(num1) + int(num2)
    if operators == '+':
        result = int(num1) + int(num2)
    if operators == '+':
        result = int(num1) + int(num2)

    #3. 응답
    return Response()