from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Post.views import PostViewSet,UserViewSet
from rest_framework.routers import DefaultRouter
from FriendRequest.views import FriendViewSet
from Comment.views import CommentViewSet
from Vote.views import VoteViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'friends',FriendViewSet,basename='friends')
router.register(r'votes',VoteViewSet)
urlpatterns =router.urls