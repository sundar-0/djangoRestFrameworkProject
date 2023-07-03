from .models import  Faculty
from .serializers import FacultySerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
class FacultyList(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['faculty_id','faculty_name']
class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyCreate(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyUpdate(generics.RetrieveUpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyReadDelete(generics.RetrieveDestroyAPIView):  
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

