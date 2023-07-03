from posts.serializers import PostSerializer
from django.shortcuts import render
from rest_framework import viewsets,status,permissions
from . models import Post
from user_profile.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
