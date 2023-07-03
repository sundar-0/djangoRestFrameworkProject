"""

I am Using Model Serialization Here..

"""
from rest_framework import serializers
from . models import  Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
        extra_kwargs = {'faculty_name': {'required': True}}

