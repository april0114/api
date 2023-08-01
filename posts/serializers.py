from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Post, Comment


class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields = '__all__'
        #fields = ['id','title', 'content']


class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'id',
            'created_at',
            'view_count',
            'writer',

        ]
        #fields = ['id','title', 'content']
        dept = 1

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',

        ]


class PostDeleteeModelSerializer(PostBaseModelSerializer):
    pass
        #fields
        #  = ['id','title', 'content']

class CommentHyperlinkModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'