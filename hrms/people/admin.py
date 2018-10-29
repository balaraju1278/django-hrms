from django.contrib import admin
from people.models import Department,Employee,EmpDesignation,EmpContactInfo,EmpMailingAddress,EmpBankInfo
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)
    list_filter = ('name', 'code',)
    
admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_code', 'pref_name', 'department', )
    list_filter = ('department',)
    
admin.site.register(Employee, EmployeeAdmin)


class EmpDesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'employee', 'department',)
    list_filter = ('department',)
    
admin.site.register(EmpDesignation, EmpDesignationAdmin)


class EmpContactInfoAdmin(admin.ModelAdmin):
    list_display = ('employee', 'contact_email', 'contact_number',)

    
admin.site.register(EmpContactInfo, EmpContactInfoAdmin)


class EmpMailingAddressAdmin(admin.ModelAdmin):
    list_display = ('employee', 'door_num', 'street', 'city', 'state',)
    
admin.site.register(EmpMailingAddress,EmpMailingAddressAdmin)


class EmpBankInfoAdmin(admin.ModelAdmin):
    list_display = ('bank_account_number', 'ifsc_code', 'bank_name', 'pan_num', 'employee',)

    
admin.site.register(EmpBankInfo, EmpBankInfoAdmin)
