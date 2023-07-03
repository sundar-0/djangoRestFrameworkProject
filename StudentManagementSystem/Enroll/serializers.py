"""

I am Using Model Serialization Here..

"""
from rest_framework import serializers
from . models import  Enroll

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = '__all__'
        extra_kwargs = {'student': {'required': True},'faculty': {'required': True},'program': {'required': True},'college': {'required': True}}
    

class EnrollListSerializer(serializers.ModelSerializer):
    student=serializers.StringRelatedField()
    college=serializers.StringRelatedField()
    faculty=serializers.StringRelatedField()
    program=serializers.StringRelatedField()
    class Meta:
        model = Enroll
        fields = '__all__'