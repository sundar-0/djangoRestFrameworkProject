"""

I am Using Model Serialization Here..

"""
from rest_framework import serializers
from . models import  Program

class ProgramListSerializer(serializers.ModelSerializer):
    faculty=serializers.StringRelatedField()
    class Meta:
        model = Program
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
        extra_kwargs = {'program_name': {'required': True}}
    