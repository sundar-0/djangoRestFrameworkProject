from django.db import models

# Create your models here.

class GraduatedStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_graduated=True)
class NonGraduatedStudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_graduated=False)

class Student(models.Model):
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others')
    )
    student_id=models.AutoField(primary_key=True,default=None)
    first_name=models.CharField(max_length=50,null=False,blank=False,default=None)
    last_name=models.CharField(max_length=50,null=False,blank=False,default=None)
    gender = models.CharField(
        max_length = 20,
        choices = options,
        default = 'male',
        null=False,
        blank=False
        )
    dob=models.DateField(null=True,blank=True,default=None)
    phone=models.CharField(max_length=20,null=True,blank=True)
    student_image=models.ImageField(upload_to="student_image",null=True,blank=True)
    date_joined=models.DateField(auto_now_add=True)
    is_graduated=models.BooleanField(default=False)
    graduated_year=models.DateField(blank=True,null=True)

    # graduated_students=GraduatedStudentManager()
    # non_graduated_students=NonGraduatedStudentManager()

    def __str__(self):
        return self.first_name

    