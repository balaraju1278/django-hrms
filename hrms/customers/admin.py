from django.contrib import admin
from .models import Customer,CustomerProject, CustomerBilling, CustomerInvoice
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person',
                    'contact_email', 'contact_number')
    
    list_filter = ('company_domain', 'company_type')
    
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerProject)
admin.site.register(CustomerBilling)
admin.site.register(CustomerInvoice)