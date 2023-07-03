# from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_patterns
# # from . views import PostList,PostDetail,UserList,UserDetail
# from . import views
# from rest_framework.routers import DefaultRouter
# from FriendRequest import views


# router = DefaultRouter()
# router.register(r'posts', views.PostViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'posts',views.FriendRequestViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
# ]


# # urlpatterns = format_suffix_patterns([
# #     path('posts/',PostList.as_view() ,name='post-list'),
# #     path('posts/<int:pk>/',PostDetail.as_view() ,name='post-detail'),
# #     path('users/', UserList.as_view(), name='user-list'),
# #     path('users/<int:pk>/',UserDetail.as_view() ,name='user-detail')
# # ])