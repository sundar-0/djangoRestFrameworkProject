"""

I am Using Model Serialization Here..

"""
from rest_framework import serializers
from . models import  Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'first_name': {'required': True},'last_name':{'required':True}}


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    

