from Faculty.models import Faculty
from django.db import models

# Create your models here.

class Program(models.Model):
    program_id=models.AutoField(primary_key=True,default=None)
    program_name=models.CharField(max_length=200,null=False,blank=False,default=None,unique=True)
    faculty=models.ForeignKey(Faculty,on_delete=models.RESTRICT,default=None,related_name="program_faculty")
    def __str__(self):
        return self.program_name
    
