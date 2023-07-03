from .models import College
from .serializers import CollegeSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
class CollegeFilter(filters.FilterSet):
    college_name=filters.CharFilter(field_name='college_name',lookup_expr='icontains')
    class Meta:
        model=College
        fields = {
       'college_name'
        }  
class CollegeList(generics.ListAPIView):
    queryset =College.objects.all()
    permission_classes=[AllowAny]
    serializer_class =CollegeSerializer
    filter_class=CollegeFilter
class CollegeCreate(generics.CreateAPIView):
    permission_classes=[AllowAny]
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeUpdate(generics.RetrieveUpdateAPIView):
    permission_classes=[AllowAny]
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeReadDelete(generics.RetrieveDestroyAPIView):
    permission_classes=[AllowAny]
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
