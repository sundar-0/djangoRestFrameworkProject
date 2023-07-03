from .models import College
from django.contrib import admin

# Register your models here.
# admin.site.register(College)

@admin.register(College)
class AdminCollegeModel(admin.ModelAdmin):
    list_display=('college_id','college_name','college_location')
