from django.urls import path
from .views import CollegeList,CollegeCreate,CollegeUpdate,CollegeReadDelete
urlpatterns = [
path('', CollegeList.as_view()),
path('add/',CollegeCreate.as_view()),
path('<int:pk>/', CollegeReadDelete.as_view()),
path('update/<int:pk>/',CollegeUpdate.as_view())
]

