from .models import Program
from django.contrib import admin

# Register your models here.
@admin.register(Program)
class ProgramAdminModel(admin.ModelAdmin):
    list_display=('faculty','program_id','program_name')

