from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ['name']

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('user',)
	list_filter = ['user']

class AssignedShiftAdmin(admin.ModelAdmin):
	list_display = ('employee', 'day', 'start_time', 'end_time')
	list_filter = ['employee']

class PreferredShiftAdmin(admin.ModelAdmin):
	list_display = ('employee', 'day', 'start_time', 'end_time')
	list_filter = ['employee']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(AssignedShift, AssignedShiftAdmin)
admin.site.register(PreferredShift, PreferredShiftAdmin)

