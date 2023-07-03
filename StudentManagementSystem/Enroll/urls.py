from django.urls import path
from .views import EnrollCreate, EnrollList, EnrollReadDelete, EnrollUpdate
urlpatterns = [
path('', EnrollList.as_view()),
path('add/',EnrollCreate.as_view()),
path('update/<int:pk>/',EnrollUpdate.as_view()),
path('<int:pk>/', EnrollReadDelete.as_view()),   
]