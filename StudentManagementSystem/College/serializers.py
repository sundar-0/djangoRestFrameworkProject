"""

I am Using Model Serialization Here..

"""
from rest_framework import serializers
from . models import College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        extra_kwargs = {'college_name': {'required': True},'college_location':{'required':True}}
    

    