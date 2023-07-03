from Post.models import Post
from Vote.models import Vote
from Comment.models import Comment
from django.shortcuts import render
from rest_framework import permissions, request
from django.contrib.auth.models import User
from Post.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets

from . permissions import hasSelfVotedOrReadOnly

from . serializers import VoteSerializer


# Create your views here.

class VoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [hasSelfVotedOrReadOnly]

    def perform_create(self, serializer):
        print(self.request.data)
        post_instance=Post.objects.get(pk=self.request.data['post'])
        print(post_instance)
        print(self.request.data['up_vote'])
        if self.request.data['up_vote']:
            serializer.save(up_vote_by=self.request.user,post=post_instance)  
        elif self.request.data['down_vote']:
            serializer.save(down_vote_by=self.request.user,post=post_instance)
           
        
        

