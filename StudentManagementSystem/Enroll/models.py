from College.models import College
from Program.models import Program
from Faculty.models import Faculty
from Student.models import Student
from django.db import models

# Create your models here.

class Enroll(models.Model):
    enroll_id=models.AutoField(primary_key=True,default=None)
    student=models.OneToOneField(Student,on_delete=models.PROTECT,default=None,related_name="enroll_student")
    faculty=models.ForeignKey(Faculty,on_delete=models.PROTECT,default=None,related_name="enroll_faculty")
    program=models.ForeignKey(Program,on_delete=models.PROTECT,default=None,related_name="enroll_program")
    college=models.ForeignKey(College,on_delete=models.PROTECT,default=None,related_name="enroll_college")


