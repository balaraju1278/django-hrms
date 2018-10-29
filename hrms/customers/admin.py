from django.contrib import admin
from .models import Customer,CustomerProject, CustomerBilling, CustomerInvoice
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerProject)
admin.site.register(CustomerBilling)
admin.site.register(CustomerInvoice)