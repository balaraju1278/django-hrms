"""
    Author: Bala
    Description: Emplooye Admin models lives here
    models:
            DepartmentAdmin: department information
            EmployeeAdmin: emplooyes general information
            EmpDesignationAdmin: emplooye desgination information
            EmpContactInfoAdmin: emplooye contact information
            EmpMailingAddressAdmin: emplooye mailing address information
            EmpBankInfoAdmin: emplooye bank details information
            EmpSkillProfileAdmin: emplooye skill profile information
    
    note: feture actions need to impliment
"""

from django.contrib import admin
from people.models import (Department,
                           Employee,
                           EmpDesignation,
                           EmpContactInfo,
                           EmpMailingAddress,
                           EmpBankInfo,
                           EmpSkillProfile)
# Register your models here.


def send_leave_info_to_all_employees(modeladmin, request, queryset):
    """
        inform all employees about public holiday before
    """
    pass


def send_customer_visit_info(modeladmin, request, queryset):
    """
        inform all employees about customer info earlier
        ex: timings, guidelines,
    """
    pass


def send_investor_visit_info(modeladmin, request, queryset):
    """
        inform all employees about invesoer info earlier
        ex: timings, guidelines,
    """
    pass


def send_general_info_(modeladmin, request, queryset):
    """
        inform all employees ant general,
        ex: events, awards, confs etc etc.
    """


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    list_filter = ('name', 'code',)
    actions = []
    
admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_code', 'pref_name', 'department', )
    list_filter = ('department',)
    actions = []
    
admin.site.register(Employee, EmployeeAdmin)


class EmpDesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 
                    'employee', 'department',)
    list_filter = ('department',)
    actions = []
    
admin.site.register(EmpDesignation, EmpDesignationAdmin)


class EmpContactInfoAdmin(admin.ModelAdmin):
    list_display = ('employee', 'contact_email', 
                    'contact_number',)
    actions = []
    
admin.site.register(EmpContactInfo, EmpContactInfoAdmin)


class EmpMailingAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'door_num', 
                    'street', 'city', 'state',)
    
    actions = []    
    
admin.site.register(EmpMailingAddress,EmpMailingAddressAdmin)


class EmpBankInfoAdmin(admin.ModelAdmin):
    list_display = ('bank_account_number', 'ifsc_code', 
                    'bank_name', 'pan_num', 'employee',)
   
    actions = []
    
admin.site.register(EmpBankInfo, EmpBankInfoAdmin)


class EmpSkillProfileAdmin(admin.ModelAdmin):
    list_display = ('emplooye', 'primary_skills',
                    'secondary_skills', 'management_skills', 
                    'languages')
    actions = []
admin.site.register(EmpSkillProfile, EmpSkillProfileAdmin)