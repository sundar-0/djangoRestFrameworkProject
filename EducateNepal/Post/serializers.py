from Vote.serializers import VoteSerializer
from django.db.models.query import QuerySet
from . models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
from Comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    comments=CommentSerializer(many=True,read_only=True)
    votes=VoteSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'post','post_image','category','post_date','comments','votes']

class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    # posts = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='post-detail'
    # )
    posts=PostSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id','username','posts']

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['password']