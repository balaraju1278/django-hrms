"""
    Author: Bala
    Description: Emplooye Forms lives here
    models:
            DepartmentForm: department information
            EmployeeForm: emplooyes general information
            EmpDesignationForm: emplooye desgination information
            EmpContactInfoForm: emplooye contact information
            EmpMailingAddressForm: emplooye mailing address information
            EmpBankInfoForm: emplooye bank details information
            EmpSkillProfileForm: emplooye skill profile information
    
    note: feture actions need to impliment
"""

from __future__ import unicode_literals


from django import forms
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import  Textarea



from people.models import (Department,
                           Employee,
                           EmpDesignation,
                           EmpContactInfo,
                           EmpMailingAddress,
                           EmpBankInfo,
                           EmpSkillProfile)

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
                'salary','picture', 'joined_date'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'size': '50'}),
            'last_name': forms.TextInput(attrs={'size': '50'}),
            'pref_name': forms.TextInput(attrs={'size': '50'}),
               
        }
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'pref_name': _('Enter Pref Name'),
            'gender': _('Select Gender'),
            'date_of_birth': _('Enter Date of Birth'),
            'marital_status': _('Matital Status'),
            'emp_code': _('Employee ID'),
            'department': _('Department'),
            'company_email': _('Company Email ID'),
            'salary' : _('Salary'),
            'picture': _('Picture'),
        }
        error_messages = {
            'first_name': {
                'max_length': _("This writer's name is too long."),
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'special'})
        self.fields['last_name'].widget.attrs.update({'class': 'special'})
        self.fields['pref_name'].widget.attrs.update({'class': 'special'})
        self.fields['gender'].widget.attrs.update({'class': 'special'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'special'})
        self.fields['marital_status'].widget.attrs.update({'class': 'special'})
        self.fields['emp_code'].widget.attrs.update({'class': 'special'})
        self.fields['department'].widget.attrs.update({'class': 'special'})
        self.fields['company_email'].widget.attrs.update({'class': 'special'})
        self.fields['salary'].widget.attrs.update({'class': 'special'})
        self.fields['picture'].widget.attrs.update({'class': 'special'})
        self.fields['joined_date'].widget.attrs.update({'class': 'special'})
    
    def clean_first_name(self):
        ln_inst = self.cleaned_data.get("last_name")
        fn_inst = self.cleaned_data.get("first_name")
        if fn_inst == ln_inst:
            raise forms.ValidationError("First name and last name sould be different")
        return ln_inst
    
    def clean_last_name(self):
        ln_inst = self.cleaned_data.get("last_name")
        fn_inst = self.cleaned_data.get("first_name")
        if fn_inst == ln_inst:
            raise forms.ValidationError("First name and last name sould be different")
        return ln_inst
    
    def clean_pref_name(self):
        pref_name_inst = self.cleaned_data.get("pref_name")
        validate = self.__class__._meta.model.objects.filter(pref_name=pref_name_inst).exists()
        if validate:
            raise forms.ValidationError("Duplicate Pref Name")
        return pref_name_inst
    
    def clean_emp_code(self):
        emp_code_i = self.cleaned_data.get('emp_code')
        validate = self.__class__._meta.model.objects.filter(emp_code=emp_code_i).exists()
        if validate:
            raise forms.ValidationError("Duplicate EMP CODE")
        return emp_code_i
    
    def clean_company_email(self):
        email_inst = self.cleaned_data.get('company_email')
        validate = self.__class__._meta.model.objects.filter(company_email=email_inst).exists()
        if validate:
            raise forms.ValidationError("Duplicate Company Email")
        return email_inst
    

class EmpDesignationForm(forms.ModelForm):
    
    class Meta:
        model = EmpDesignation
        fields = ('title', 'code', 'employee', 'department')
        labels = {
             'title': _('Enter designation of Employee'),
             'code': _('Enter code for designation level'),
             'employee': _('Employee'),
             'department': _('Department'),
        }
        help_texts = {
            
        }
        error_messages = {
            
        }
        
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'special'})
        self.fields['code'].widget.attrs.update({'class': 'special'})
        self.fields['employee'].widget.attrs.update({'class': 'special'})
        self.fields['department'].widget.attrs.update({'class': 'special'})
        
    def clean_code(self):
        code_inst = self.cleaned_data.get("code")
        validate = self.__class__._meta.model.objects.filter(code=code_inst).exists()
        if validate:
            raise forms.ValidationError("Duplicate Code")
        return code_inst
        
        
class DepartmentForm(forms.ModelForm):
    
    class Meta:
        model = Department
        fields = ('name', 'code', 'department_head', 'department_head_mail')
        widgets = {
            
        }
        labels = {
             'name': _('Enter Department Name'),
             'code': _('Enter Departent Code'),
        }
        help_texts = {
                    
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'special'})
        self.fields['code'].widget.attrs.update({'class': 'special'})
        self.fields['department_head'].widget.attrs.update({'class': 'special'})
        self.fields['department_head_mail'].widget.attrs.update({'class': 'special'})
    
    def clean_code(self):
        code_inst = self.cleaned_data.get("code")
        validate = self.__class__._meta.model.objects.filter(code=code_inst).exists()
        if validate:
            raise forms.ValidationError("Please Enter Valid Department Code")
        return code_inst
    
    def clean_name(self):
        name_inst = self.cleaned_data.get("name")
        validate = self.__class__._meta.model.objects.filter(\
                        Q(name=self.name_inst)|Q(name__icontains=self.name_inst)).exists()    
        if validate:
            raise forms.ValidationError("Department Already Exists")
        return name_inst
        
    def clean_department_head(self):
        head_inst = self.cleaned_data.get("department_head")
        validate = self.__class__._meta.model.objects.filter(department_head=self.head_inst).exists()
        if validate:
            raise forms.ValidationError("Employee already head for other departments")
        return head_inst
    
    def clean_department_head_mail(self):
        mail_inst = self.cleaned_data.get("department_head_mail")
        validate = self.__class__._meta.model.objects.filter(department_head_mail=mail_inst).exists()
        if validate:
            raise forms.ValidationError("Please Enter Valid Email")
        return mail_inst


class EmpContactInfoForm(forms.ModelForm):

    class Meta:
        model = EmpContactInfo
        fields = ('contact_email', 'contact_number', 'linkedin', 
                  'github','facebook', 'blog', 'employee')
        widgets = {
            
        }
        labels = {
            
        }
        help_texts = {
                    
        }
        error_messages = {
            
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['contact_email'].widget.attrs.update({'class': 'special'})
        self.fields['contact_number'].widget.attrs.update({'class': 'special'})
        self.fields['linkedin'].widget.attrs.update({'class': 'special'})
        self.fields['github'].widget.attrs.update({'class': 'special'})
        self.fields['facebook'].widget.attrs.update({'class': 'special'})
        self.fields['blog'].widget.attrs.update({'class': 'special'})
        self.fields['employee'].widget.attrs.update({'class': 'special'})


    def clean_contact_email(self):
        email_inst = self.cleaned_data.get("contact_email")
        validate = self.__class__._meta.model.objects.filter(contact_email=email_inst).exists()
        if validate:
            raise forms.ValidationError("Found Duplicate Email Id")
        return email_inst
    
    def clean_contact_number(self):
        num_inst = self.cleaned_data.get("contact_number")
        validate = self.__class__._meta.model.objects.filter(contact_number=num_inst).exists()
        if validate:
            raise forms.ValidationError("Found Duplicate Contact Number")
        return num_inst


class EmpMailingAddressForm(forms.ModelForm):
    
    class Meta:
        model = EmpMailingAddress
        fields = '__all__'
        widgets = {
                
        }
        labels = {
             
        }
        help_texts = {
               
        }
        error_messages = {
            
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['door_num'].widget.attrs.update({'class': 'special'})
        self.fields['street'].widget.attrs.update({'class': 'special'})
        self.fields['city'].widget.attrs.update({'class': 'special'})
        self.fields['state'].widget.attrs.update({'class': 'special'})
        self.fields['country'].widget.attrs.update({'class': 'special'})
        self.fields['pincode'].widget.attrs.update({'class': 'special'})
        self.fields['employee'].widget.attrs.update({'class': 'special'})
        

class EmpBankInfoForm(forms.ModelForm):
    
    class Meta:
        model = EmpBankInfo
        fields = '__all__'
        widgets = {
                 
        }
        labels = {
             
        }
        help_texts = {
                   
        }
        error_messages = {
            
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['bank_account_number'].widget.attrs.update({'class': 'special'})
        self.fields['ifsc_code'].widget.attrs.update({'class': 'special'})
        self.fields['bank_name'].widget.attrs.update({'class': 'special'})
        self.fields['pan_num'].widget.attrs.update({'class': 'special'})
        self.fields['employee'].widget.attrs.update({'class': 'special'})
    
    def clean_bank_account_number(self):
        ban = self.cleaned_data.get("bank_account_number")
        validate = self.__class__._meta.model.objects.filter(bank_account_number=ban).exists()
        if validate:
            raise forms.ValidationError("Duplicate Bank account number")
        return ban
    
    def clean_pan_num(self):
        pan = self.cleaned_data.get("pan_num")
        validate = self.__class__._meta.model.objects.filter(pan_num=pan).exists()
        if validate:
            raise forms.ValidationError("Duplicate PAN ID")
        return pan


class EmpSkillProfileForm(forms.ModelForm):
    
    class Meta:
        model = EmpSkillProfile
        fields = '__all__'
        widgets = {
                
        }
        labels = {
            
        }
        help_texts = {
                   
        }
        error_messages = {
           
        }
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['emplooye'].widget.attrs.update({'class': 'special'})
        self.fields['working_department'].widget.attrs.update({'class': 'special'})
        self.fields['primary_skills'].widget.attrs.update({'class': 'special'})
        self.fields['secondary_skills'].widget.attrs.update({'class': 'special'})
        self.fields['management_skills'].widget.attrs.update({'class': 'special'})
        self.fields['languages'].widget.attrs.update({'class': 'special'})
        self.fields['expert_in_domain'].widget.attrs.update({'class': 'special'})
    
    def clean_expert_in_domain(self):
        # logic expertr in domain skill should be in primary skills
        pass
    
    def clean_primary_skills(self):
        #pm = self.cleaned.data.get("primary_skills")
        pass
    
    
    def clean_secondary_skills(self):
        pass
    
    def clean_management_skills(self):
        pass
    