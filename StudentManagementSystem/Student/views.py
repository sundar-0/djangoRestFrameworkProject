import django_filters
from .models import  Student
from .serializers import StudentSerializer,StudentListSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
class StudentFilter(filters.FilterSet):
    first_name=filters.CharFilter(field_name='first_name',lookup_expr='icontains')
    class Meta:
        model=Student
        fields = {
        'first_name'
        }  
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

   
class StudentCreateUpdate(APIView):
    parser_classes = [MultiPartParser, FormParser] 
    def post(self, request, format=None):
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        student=Student.objects.get(pk=pk)
        print(student)
        serializer = StudentListSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class StudentReadDelete(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
