from django.urls import path,include
urlpatterns = [
path('college/',include('College.urls')),
path('faculty/',include('Faculty.urls')),
path('program/',include('Program.urls')),
path('student/',include('Student.urls')),
path('student/enroll/',include('Enroll.urls'))
]

