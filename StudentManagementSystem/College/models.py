from django.db import models

# Create your models here.

class College(models.Model):
    college_id=models.AutoField(primary_key=True,default=None)
    college_name=models.CharField(max_length=200,null=False,blank=False,default=None,unique=True)
    college_location=models.CharField(max_length=200,null=False,blank=False,default=None)
    def __str__(self):
        return self.college_name
    
       
