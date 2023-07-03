from django.urls import path
from .views import FacultyList,FacultyReadDelete,FacultyCreate,FacultyUpdate
urlpatterns = [
path('', FacultyList.as_view()),
path('add/',FacultyCreate.as_view()),
path('<int:pk>/', FacultyReadDelete.as_view()),   
path('update/<int:pk>/',FacultyUpdate.as_view())
]