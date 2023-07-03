from .filters import EnrollFilter
from .models import  Enroll
from .serializers import EnrollSerializer,EnrollListSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class EnrollList(generics.ListAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EnrollFilter
    


class EnrollCreate(generics.CreateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer



class EnrollUpdate(generics.RetrieveUpdateAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer


class EnrollReadDelete(generics.RetrieveDestroyAPIView):
    queryset = Enroll.objects.all()
    serializer_class = EnrollListSerializer




