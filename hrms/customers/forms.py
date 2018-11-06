from django import forms
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from .models import (Customer,
                     CustomerProject, 
                     CustomerBilling, 
                     CustomerInvoice)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {}
        widgets = {}
        error_messages = {}
    
    def __init__(self, *args, **kwargs):
        pass
    
    def clean_company_name(self):
        pass
    
    def clean_contact_person(self):
        pass
    
    def clean_contact_email(self):
        pass
    
    def clean_contact_number(self):
        pass
    
    def clean_alt_email(self):
        pass
    
    def clean_alt_num(self):
        pass
