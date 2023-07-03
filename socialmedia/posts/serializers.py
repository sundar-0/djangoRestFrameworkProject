from comments.serializers import CommentSerializer
from django.db.models import fields
from posts.models import Post
from rest_framework import serializers
from votes.serializers import VoteSerializer
class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    votes=VoteSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields=('id','content','post_image','category','post_date','comments','votes')
        