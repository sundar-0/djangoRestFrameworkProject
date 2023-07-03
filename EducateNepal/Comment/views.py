from Comment.models import Comment
from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
from Post.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets

from . serializers import CommentSerializer


# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

