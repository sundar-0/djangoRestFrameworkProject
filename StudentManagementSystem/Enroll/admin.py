from .models import Enroll
from django.contrib import admin

# Register your models here.
@admin.register(Enroll)
class EnrollAdminModel(admin.ModelAdmin):
    list_display=('enroll_id','student','faculty','program','college')