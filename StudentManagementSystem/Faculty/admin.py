from College.models import College
from Program.models import Program
from .models import Faculty
from django.contrib import admin

# Register your models here.
class ProgramInline(admin.TabularInline):
    model = Program
@admin.register(Faculty)
class FacultyAdminModel(admin.ModelAdmin):
    inlines = [
        ProgramInline,
    ]
    list_display=('faculty_id','faculty_name')

