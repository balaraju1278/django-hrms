from django.contrib import admin
from .models import LeaveCategory,EmployeeLeaveProfile,LeaveApplication
# Register your models here.

admin.site.register(LeaveCategory)
admin.site.register(EmployeeLeaveProfile)


def approve_multiple(modeladmin, request, queryset):
    for leave in queryset:
        leave.status = True
        leave.save()
    
approve_multiple.short_description = "Approve All"


class LeaveAppAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'employee', 'leave_category',
                    'status', 'subject']
    list_filter = [ "leave_category"]
    date_hierarchy = "start_date"
    
    actions = [approve_multiple]

admin.site.register(LeaveApplication, LeaveAppAdmin)