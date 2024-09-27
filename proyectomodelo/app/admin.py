from django.contrib import admin
from app.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nombre','email', 'fono']

admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
