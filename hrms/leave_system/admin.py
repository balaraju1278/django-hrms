from django.contrib import admin
from .models import LeaveCategory,EmployeeLeaveProfile,LeaveApplication
# Register your models here.

admin.site.register(LeaveCategory)
admin.site.register(EmployeeLeaveProfile)
admin.site.register(LeaveApplication)