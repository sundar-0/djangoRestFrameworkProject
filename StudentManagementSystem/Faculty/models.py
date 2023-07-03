from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_id=models.AutoField(primary_key=True,default=None)
    faculty_name=models.CharField(max_length=200,null=False,blank=False,default=None,unique=True)
    def __str__(self):
        return self.faculty_name
    
       
