
from .serializers import PostSerializer,UserSerializer,PasswordSerializer
from Post.models import Post
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from . permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response



# Create your views here.

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    
  

class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

