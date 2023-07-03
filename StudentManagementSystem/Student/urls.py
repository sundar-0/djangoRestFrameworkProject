from django.urls import path
from .views import StudentList,StudentReadDelete,StudentCreateUpdate
urlpatterns = [
path('', StudentList.as_view()),
path('add/',StudentCreateUpdate.as_view()),
path('<int:pk>/', StudentReadDelete.as_view()),   
path('update/<int:pk>/',StudentCreateUpdate.as_view())
]