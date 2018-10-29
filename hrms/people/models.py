"""
    employee models lives here
"""
# Python Imports
import re
from decimal import Decimal

from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
    ValidationError    
    )
from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

# Create your models here.


NAME_REGEX = '^[a-zA-Z]*$'

def validate_linkedin(value):
    """
        validates linkedin profile valid or not
    """
    ld_inst = value
    ld_reg = re.compile('((http(s?)://)*([a-zA-Z0-9\-])*\.|[linkedin])[linkedin/~\-]+\.[a-zA-Z0-9/~\-_,&=\?\.;]+[^\.,\s<]')
    validate = ld_reg.match(ld_inst)
    if validate == None:
        raise ValidationError(
            '%(value)s is not valid Linkedin Id',
            params={'value': value},
            )


def validate_github(value):
    pass


def validate_pan_number(value):
    """
        validates vallid PAN id or not
    """
    pan_inst = value
    pan_regex = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    validate = re.match(pan_regex, pan_inst)
    if validate == None:
        raise ValidationError(
            '%(value)s is not valid PAN number',
            params={'value': value},
            )

class Department(models.Model):
    """
        department model    
    """
    
    DEP_CHOICES = (
        ('DATA SCIENCE', 'DATA SCIENCE'),
        ('PRODUCTS', 'PRODUCTS'),
        ('OPERATIONS', 'OPERATIONS'),
        ('ADMIN', 'ADMIN')    
    )
    name = models.CharField(
            max_length=50, unique=True,
            verbose_name=_("Department Name"), 
            choices=DEP_CHOICES,
            )
    code = models.CharField(
            max_length=10,unique=True, 
            verbose_name=_('Department Code')
            )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
    def get_name(self):
        """
            returns department name
        """
        if self.name:
            return self.name
        else:
            return "n/a"
            
    def get_absolute_url(self):
        pass
        
    def validate_unique(self, *args, **kwargs):
        super(Department, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__.default_manager.filter(
            Q(name=self.name) | Q(code=self.code)        
        ) 
        if qs.exists():
            raise ValidationError(
                "Please Enter Valid name and code"            
            )
    def clean(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        if self.code:
            self.code = self.code.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Department, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Department')

 

class Employee(models.Model):
    """
        Employee model    
    """
    MALE = 'M'
    FEMALE = 'FM'
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('FM', 'Female')    
    )
    MARRIED = 'MR'
    SINGLE = 'S'
    STATUS_CHOICES = (
        ('MR', 'MARRIED'),
        ('S', 'SINGLE'),    
    )
    first_name = models.CharField(
                max_length=100, 
                verbose_name=_("First Name"), 
                blank=True, null=True,
                validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ]
                )
    last_name = models.CharField(
                max_length=100, 
                verbose_name=_("Last Name"), 
                blank=True, null=True,
                validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ])
    pref_name = models.CharField(
                max_length=100, 
                verbose_name=_("Prefer Name"), 
                blank=True, null=True,validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ])
    gender = models.CharField(
                max_length=2, 
                choices=GENDER_CHOICES, 
                verbose_name=_("Gender"))
    date_of_birth = models.DateTimeField(
                blank=True, null=True,
                verbose_name=_('Date of Birth'))
    marital_status = models.CharField(
                max_length=2, 
                verbose_name=_("Marital Status"),
                choices=STATUS_CHOICES, 
                default=SINGLE)
    emp_code = models.CharField(
                max_length=10, unique=True,
                verbose_name=_("Employee ID"),
                blank=True, null=True)
    department = models.ForeignKey(
                Department, 
                on_delete=models.CASCADE, 
                verbose_name=_("Department"))
    company_email = models.EmailField(
                max_length=100,unique=True, 
                verbose_name=_("Company Email"), 
                blank=True, null=True)
    picture = models.ImageField(
                null=True,blank=True,
                height_field='height_field',
                width_field='width_field'
                )
    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)
    joined_date = models.DateField(blank=True, verbose_name=_("Joined Data"))

    def __str__(self):
        return '{}-{}-{}'.format(self.first_name, self.last_name, self.emp_code)
    
    def get_full_name(self):
        """
            returns employee full name
        """
        if self.first_name & self.last_name:
            return '{}{}'.format(self.first_name, self.last_name)
        else:
            return self.first_name
    
    def get_pref_name(self):
        """
            returns employee preferable name
        """
        if self.pref_name:
            return "{}".format(self.pref_name)
        else:
            return "n/a"
            
    def get_emp_code(self):
        """
            returns employee code        
        """
        if self.emp_code:
            return '{}'.format(self.emp_code)
        else:
            return "n/a"
    
    def get_company_email(self):
        """
            returns employee company email
        """
        if self.company_email:
            return self.company_email
        else:
            return "n/a"
    
    def get_department(self):
        """
            returns employee department
        """
        if self.department:
            return self.department
        else:
            return "n/a"
    
    def get_date_of_birth(self):
        """
            returns human readable format of dob
        """
        return self.date_of_birth.strftime('%d, %b %Y')
    
    def validate_unique(self, *args, **kwargs):
        super(Employee, self).validate_unique(*args, **kwargs)
        
        email_qs = self.__class__.default_manager.filter(
                    company_email=self.company_email        
        )
        emp_code_qs = self.__class__.default_manager.filter(
                    emp_code=self.emp_code        
        )
        if email_qs.exists():
            raise ValidationError("Email Id Already exists with another employee")
            
        if emp_code_qs.exists():
            raise ValidationError("Employee Id Already exists with another employee")
    
    def clean(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.lower()
        if self.last_name:
            self.last_name = self.last_name.lower()
        if self.pref_name:
            self.pref_name = self.pref_name.lower()
        if self.emp_code:
            self.emo_code = self.emp_code.lower()
        if self.company_email:
            self.company_email = self.company_email.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
        

class EmpDesignation(models.Model):
    """
        employee designation/job title model    
    """
    title = models.CharField(
            max_length=50, 
            verbose_name=_("Designation"))
    code = models.CharField(
            max_length=10, 
            verbose_name=_('Department Code')
            )
    employee = models.ForeignKey(
                    Employee, 
                    on_delete=models.CASCADE, 
                    verbose_name=_("Employee"))
    department = models.ForeignKey(
                    Department,
                    on_delete=models.CASCADE,
                    verbose_name=_("Department")
                        
                    )
                    
    def __str__(self):
        return '{}-{}'.format(self.user, self.title)
    
    def get_user_title(self):
        """
            returns designation 
        """
        if self.title:
            return self.title
        else:
            return "n/a"
    
    def get_employee(self):
        """
            returns employee name
        """
        if self.employee:
            return str(self.employee)
        else:
            return "n/a"
    
    def get_deartment(self):
        """
            returns employee departments
        """
        if self.department:
            return self.department
        else:
            return "n/a"
            
    def get_employee_code(self):
        """
            returns employee code
        """
        if self.code:
            return self.code
        else:
            return "n/a" 

    def clean(self, *args, **kwargs):
        if self.title:
            self.title = self.title.lower()
        if self.code:
            self.code = self.code.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(EmpDesignation, self).save(*args,**kwargs)
        
    class Meta:
        verbose_name = _("Designtion")
        verbose_name_plural = _("Designation")
    

        
class EmpContactInfo(models.Model):
    """
        employee contact info    
    """
    contact_email = models.EmailField(
                    max_length=100, unique=True,
                    verbose_name=_("Contact Email"), 
                    blank=True, null=True)
    contact_number = models.CharField(
                    max_length=10, unique=True,
                    verbose_name=_("Contact Number"),
                    blank=True, null=True)
    linkedin = models.CharField(
                    validators=[validate_linkedin],
                    max_length=150, unique=True,
                    verbose_name=_("LinkedIn ID"), 
                    blank=True, null=True) 
    github = models.CharField(
                    max_length=150, unique=True,
                    verbose_name=_("Github ID"), 
                    blank=True, null=True)
    facebook = models.CharField(
                    max_length=150, unique=True,
                    verbose_name=_("Facebook"), 
                    blank=True, null=True)
    blog = models.CharField(
                    max_length=150, unique=True,
                    verbose_name=_("Personal Blog"), 
                    blank=True, null=True)
    employee = models.ForeignKey(
                    Employee, 
                    on_delete=models.CASCADE, 
                    verbose_name="Employee")

    def __str__(self):
        return str(self.employee)
    
    def get_contact_email(self):
        """
            returns employee contact email
        """
        if self.contact_email:
            return self.contact_email
        else:
            return "n/a"
    
    def get_contact_number(self):
        """
            returns employee contact number
        """
        if self.contact_number:
            return self.contact_number
        else:
            return "n/a"
    def validate_unique(self, *args, **kwargs):
        super(EmpContactInfo, self).validate_unique(*args, **kwargs)
        
        email_qs = self.__class__.default_manager.filter(
            contact_email=self.contact_email        
        )
        number_qs = self.__class__.default_manager.filter(
            contact_number=self.contact_number        
        )
        
        if email_qs.exists():
            raise ValidationError("Duplicate email")
        
        if number_qs.exists():
            raise ValidationError("Duplicate Number")
                
    def clean(self, *args, **kwargs):
        if self.contact_email:
            self.contact_email = self.contact_email.lower()
        if self.linkedin:
            self.linkedin = self.linkedin.lower()
        if self.github:
            self.github = self.github.lower()
        if self.facebook:
            self.facebook = self.facebook.lower()
        if self.blog:
            self.blog = self.blog.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(EmpContactInfo, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Employees Contact Information'
        verbose_name_plural = 'Employees Contact Information'
        
        
class EmpMailingAddress(models.Model):
    """
        employee mailing address
    """
    door_num = models.CharField(
                max_length=6, 
                blank=True, null=True, 
                verbose_name=_("Door Number"))
    street = models.CharField(
                max_length=15, 
                blank=True, null=True, 
                verbose_name=_("Street Name"))
    city = models.CharField(
                max_length=40, 
                blank=True, null=True, 
                verbose_name=_("City"),
                validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ])
    state = models.CharField(
                max_length=50, 
                blank=True, null=True, 
                verbose_name=_("State"),
                validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ])
    country = models.CharField(
                max_length=50, 
                blank=True, null=True, 
                verbose_name=_("Country"),
                validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ])
    pincode = models.CharField(
                max_length=6, 
                blank=True, null=True, 
                verbose_name=_("Pincode"))
    employee = models.ForeignKey(
                Employee, 
                on_delete=models.CASCADE, 
                verbose_name=_("Employee"))
    
    def __str__(self):
        return str(self.employee)
    

    def clean(self, *args, **kwargs):
        if self.street:
            self.street = self.street.lower()
        if self.city:
            self.city = self.city.lower()
        if self.state:
            self.state = self.state.lower()
        if self.country:
            self.country = self.country.lower()
    
    def save(self, *args,  **kwargs):
        self.full_clean()
        super(EmpMailingAddress, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Employee Mailing Address')
        verbose_name_plural = _("Employee Mailing Address")


class EmpBankInfo(models.Model):
    bank_account_number = models.PositiveIntegerField(
                            unique=True,
                            blank=True,null=True,
                            verbose_name=_("Bank Account Number"),
                            validators = [
                                MinValueValidator(10000000),
                                MaxValueValidator(99999999)
                            ])
    ifsc_code = models.CharField(
                        max_length=50, 
                        blank=True, null=True,
                        verbose_name=_("Bank IFSC Code"))
    bank_name = models.CharField(
                        max_length=50, 
                        blank=True, null=True,
                        verbose_name=_("Bank Name"))
    pan_num = models.CharField(
                        validators=[validate_pan_number],        
                        max_length=50, unique=True,
                        blank=True, null=True,
                        verbose_name=_("PAN ID"))
    employee = models.ForeignKey(
                Employee, 
                on_delete=models.CASCADE, 
                verbose_name=_("Employee"))
    
    def __str__(self):
        return str(self.employee)
    
    def get_bank_account_number(self):
        """
            returns employee bank account number
        """
        if self.bank_account_number:
            return self.bank_account_number
        else:
            return "n/a"
    
    def get_pan_num(self):
        """
            returns employee pan id
        """
        if self.pan_num:
            return self.pan_num
        else:
            return "n/a"
            
    def validate_unique(self, *args, **kwargs):
        super(EmpBankInfo, self).validate_unique(*args, **kwargs)
        
        b_qs = self.__class__.default_manager.filter(
            bank_account_number=self.bank_account_number        
        )
        p_qs = self.__class__.default_manager.filter(
            pan_num=self.pan_num        
        )
        
        if b_qs.exists():
            raise ValidationError("Duplicate Bank Account Number")
        
        if p_qs.exists():
            raise ValidationError("Duplicate PAN Number")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super(EmpBankInfo, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _("Employees Bank Details")
        verbose_name_plural = _("Employees Bank Details")