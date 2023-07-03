from . models import Enroll
from django_filters import rest_framework as filters
class EnrollFilter(filters.FilterSet):
    student=filters.CharFilter(field_name='student__first_name',lookup_expr='icontains')
    program=filters.CharFilter(field_name='program__program_name')
    faculty=filters.CharFilter(field_name='faculty__faculty_name')
    college=filters.CharFilter(field_name='college__college_name')
    class Meta:
        model=Enroll
        fields = {
        'student',
        'program',
        'faculty',
        'college'
        }  