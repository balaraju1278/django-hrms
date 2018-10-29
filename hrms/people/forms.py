from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _


from people.models import Department,Employee, EmpDesignation,EmpContactInfo,EmpMailingAddress,EmpBankInfo


class EmployeeForm(forms.ModelForm):
    """
        Employee creation form
    """
    class Meta:
        model = Employee
        fields = (
                'first_name', 'last_name', 'pref_name',
                'gender', 'date_of_birth', 'marital_status',
                'emp_code', 'department', 'company_email',
                'picture', 'joined_date'
        )
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['pref_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['marital_status'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control'})
        self.fields['joined_date'].widget.attrs.update({'class': 'form-control'})
    
    def clean_emp_code(self):
        pass
    
    def clean_company_email(self):
        pass
    

class EmpDesignation(forms.ModelForm):
    pass