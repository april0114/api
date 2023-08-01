from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostBaseModelSerializer, PostListModelSerializer, PostCreateModelSerializer, CommentHyperlinkModelSerializer, PostDeleteeModelSerializer
# Create your views here.

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentHyperlinkModelSerializer

@api_view()
def calculator(request):
    #1. 데이터 확인
    num1 = request.GET.get('num1',0)
    num2 = request.GET.get('num2',0)
    operators = request.GET.get('operators')

    #2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    if operators == '*':
        result = int(num1) * int(num2)
    if operators == '-':
        result = int(num1) - int(num2)
    if operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

        data = {
            'type':'FBV',
            'result': result
        }

    #3. 응답
    return Response()

class CalculatorAPIView(APIView):
    def get(self, request):
            num1 = request.GET.get('num1',0)
            num2 = request.GET.get('num2',0)
            operators = request.GET.get('operators')

    #2. 계산
            if operators == '+':
                result = int(num1) + int(num2)
            if operators == '*':
                result = int(num1) * int(num2)
            if operators == '-':
                result = int(num1) - int(num2)
            if operators == '/':
                result = int(num1) / int(num2)
            else:
                result = 0

            data = {
            'type':'CBV',
            'result': result
            }

    #3. 응답
            return Response()
    #def post