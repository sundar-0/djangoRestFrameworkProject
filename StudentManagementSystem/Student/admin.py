
from .models import Student
from django.contrib import admin

# Register your models here.
@admin.register(Student)
class StudentAdminModel(admin.ModelAdmin):
    list_display=('student_id','first_name','last_name','gender','dob','phone','student_image','date_joined','graduated_year','is_graduated')


