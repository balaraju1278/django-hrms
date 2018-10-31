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

from people.forms import (DepartmentForm,
                           EmployeeForm,
                           EmpDesignationForm,
                           EmpContactInfoForm,
                           EmpMailingAddressForm,
                           EmpBankInfoForm,
                           EmpSkillProfileForm)
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
    
    def view_name(self, obj):
        return obj.name
    
    def view_code(self, obj):
        return obj.code
        
    view_name.empty_value_display = '???'
    view_code.empty_value_display = '???'    
    
admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_code', 'pref_name', 'department', 
                    'gender', 'company_email', 'date_of_birth')
    list_filter = ('department',)
    
    def view_date_of_birth(self, obj):
        return obj.date_of_birth
    
    def view_emp_code(self, obj):
        return obj.emp_code
    
    def view_pref_name(self, obj):
        return obj.pref_name
    
    def view_department(self, obj):
        return obj.department
    
    def view_gender(self, obj):
        return obj.gender
    
    def view_company_email(self, obj):
        return obj.company_email
    
    view_emp_code.empty_value_display = '???'
    view_pref_name.empty_value_display = '???'
    view_department.empty_value_display = '???'
    view_gender.empty_value_display = '???'
    view_company_email.empty_value_display = '???'
    view_date_of_birth.empty_value_display = '???'
    actions = []
    form = EmployeeForm
    
admin.site.register(Employee, EmployeeAdmin)


class EmpDesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 
                    'employee', 'department',)
    list_filter = ('department',)
    actions = []
    
    def view_title(self, obj):
        return obj.title
    
    def view_code(self, obj):
        return obj.code
    
    def view_employee(self, obj):
        return obj.employee
        
    def view_department(self, obj):
        return obj.department
    
    view_title.empty_value_display = '???'
    view_code.empty_value_display = '???'
    view_employee.empty_value_display = '???'
    view_department.empty_value_display = '???'
    
admin.site.register(EmpDesignation, EmpDesignationAdmin)


class EmpContactInfoAdmin(admin.ModelAdmin):
    list_display = ('employee', 'contact_email', 
                    'contact_number',)
    actions = []
    
    def view_employee(self, obj):
        return obj.employee
    
    def view_contact_email(self, obj):
        return obj.contact_email
    
    def view_contact_number(self, obj):
        return obj.contact_number
    
    view_employee.empty_value_display = '???'
    view_contact_email.empty_value_dispaly = '???'
    view_contact_number.empty_value_dispaly = '???'
    
    
admin.site.register(EmpContactInfo, EmpContactInfoAdmin)


class EmpMailingAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'door_num', 
                    'street', 'city', 'state',)
    
    actions = []    
    
    def view_employee(self, obj):
        return obj.employee
        
    def view_door_num(self, obj):
        return obj.door_num
    
    def view_street(self, obj):
        return obj.street
    
    def view_city(self, obj):
        return obj.city
    
    def view_state(self, obj):
        return obj.state
    
    view_employee.empty_value_display = '???'
    view_door_num.empty_value_display = '???'
    view_street.empty_value_display = '???'
    view_city.empty_value_display = '???'
    view_state.empty_value_display = '???'
    
    
admin.site.register(EmpMailingAddress,EmpMailingAddressAdmin)


class EmpBankInfoAdmin(admin.ModelAdmin):
    list_display = ('bank_account_number', 'ifsc_code', 
                    'bank_name', 'pan_num', 'employee',)
   
    actions = []
    def view_bank_account_number(self, obj):
        return obj.bank_account_number
    
    def view_ifsc_code(self, obj):
        return obj.ifsc_code
    
    def view_bank_name(self, obj):
        return obj.bank_name
    
    def view_pan_num(self, obj):
        return obj.pan_num
    
    def view_employee(self, obj):
        return obj.employee
    
    view_bank_account_number.empty_value_display = '???'
    view_ifsc_code.empty_value_display = '???'
    view_bank_name.empty_value_display = '???'
    view_pan_num.empty_value_display = '???'
    view_employee.empty_value_display = '???'
    
admin.site.register(EmpBankInfo, EmpBankInfoAdmin)


class EmpSkillProfileAdmin(admin.ModelAdmin):
    list_display = ('emplooye', 'primary_skills',
                    'secondary_skills', 'management_skills', 
                    'languages')
    
    list_filter = ('primary_skills', 'secondary_skills', 'management_skills', 'languages',)
    actions = []
    
    def view_employee(self,obj):
        return obj.employee
    
    def view_primary_skills(self,obj):
        return obj.primary_skills
        
    def view_secondary_skills(self,obj):
        return obj.secondary_skills
        
    def view_management_skills(self,obj):
        return obj.management_skills
        
    def view_languages(self,obj):
        return obj.languages
        
        
    view_employee.empty_value_display = '???'
    view_primary_skills.empty_value_display = '???'
    view_secondary_skills.empty_value_display = '???'
    view_management_skills.empty_value_display = '???'
    view_languages.empty_value_display = '???'
    
admin.site.register(EmpSkillProfile, EmpSkillProfileAdmin)