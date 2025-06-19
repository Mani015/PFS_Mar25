from django.contrib import admin
from app5.models import Student
# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['Fname','Lname','Marks']

admin.site.register(Student,StudentModelAdmin)

