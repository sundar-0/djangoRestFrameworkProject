from django.urls import path
from .views import ProgramCreate, ProgramList, ProgramReadDelete, ProgramUpdate
urlpatterns = [
path('', ProgramList.as_view()),
path('add/',ProgramCreate.as_view()),
path('<int:pk>/', ProgramReadDelete.as_view()),   
path('update/<int:pk>/',ProgramUpdate.as_view())
]