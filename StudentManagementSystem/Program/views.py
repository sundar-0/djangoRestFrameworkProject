from .models import  Program
from .serializers import ProgramListSerializer,ProgramSerializer
from rest_framework import generics
from django_filters import rest_framework as filters

class ProgramFilter(filters.FilterSet):
    program_name=filters.CharFilter(field_name='program_name',lookup_expr='icontains')
    class Meta:
        model=Program
        fields = {
        'program_name'
        }  
class ProgramList(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramListSerializer
    filter_class=ProgramFilter

class ProgramCreate(generics.CreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ProgramUpdate(generics.RetrieveUpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ProgramReadDelete(generics.RetrieveDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramListSerializer
