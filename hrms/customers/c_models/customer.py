"""
    Auhtor: Bala
    Description:  customer profile models lives here
"""
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


from people.models import Employee



customer_error_messages = {

        'company_exists': "Customer Already exists with same name",
        'contact_email_exists': 'Customer Already exists with same email',
        'contact_number_exists': 'Customer Already exists with same number',
} 

def validate_company_name(value):
    """
            validates company name and dupicate exists 
    """
    comp_inst = value
    comp_check = Customer.objects.filter(company_name=comp_inst).exists()
    if comp_check:
        raise ValidationError(customer_error_messages.get('company_exists'))
    else:
        return comp_inst


def validate_contact_email(value):
    """
        validate customer contact email and duplicate exists
    """      
    email_inst = value      
    email_check = Customer.objects.filter(contact_email=value).exists()
    if email_check:
        raise ValidationError(customer_error_messages.get('contact_email_exists'))
    else:
        return email_inst


def validate_contact_number(value):
    """
        validate customer contact number and duplicate exists
    """
    number_inst = value
    number_check = Customer.objects.filter(contact_number=value).exists()
    if number_check:
        raise ValidationError(customer_error_messages.get('contact_number_exists'))
    else:
        return number_inst


class Customer(models.Model):
    """
        company customer profile model

    """

    TYPE_CHOICES = (
        ('Office', 'OFFICE'),
        ('Personal','PERSONAL')    
    )
    company_name = models.CharField(
                                    max_length=150, unique=True,
                                    verbose_name=_("Company Name"), 
                                    blank=True, null=True,
                                    validators = [validate_company_name],
                                    help_text=_("Name of Customer Company"))
    company_type = models.CharField(
                                    max_length=150, 
                                    verbose_name=_("Company Type"), 
                                    blank=True, null=True,
                                    help_text=_("Company Type ex:startup, mnc, pvt ltd"))
    company_domain = models.CharField(
                                    max_length=150, 
                                    verbose_name=_("Company Domain"), 
                                    blank=True, null=True,
                                    help_text=_("Company domain ex:finance,manufacturing"))
    contact_person = models.CharField(
                                    max_length=150, unique=True,
                                    verbose_name=_("Contact Person"), 
                                    blank=True, null=True)
    contact_email = models.EmailField(
                                    max_length=150, unique=True,
                                    validators = [validate_contact_email],
                                    verbose_name=_("Contact Email"), 
                                    blank=True, null=True)
    email_type = models.CharField(
                                    max_length=25, 
                                    verbose_name=_("Email Type"), 
                                    choices=TYPE_CHOICES, blank=True, null=True)    
    contact_number = models.CharField(
                                    max_length=12,unique=True,
                                    validators = [validate_contact_number],                                    
                                    verbose_name=_("Contact Number"),
                                    blank=True, null=True)
    number_type = models.CharField(
                                    max_length=25, 
                                    verbose_name=_("Email Type"),
                                    choices=TYPE_CHOICES,
                                    blank=True, null=True)    
    alt_email = models.EmailField(
                                    max_length=150,
                                    verbose_name=_("Alternative Email"), 
                                    blank=True,null=True)
    alt_num = models.EmailField(
                                    max_length=150,
                                    verbose_name=_("Alternative Number"), 
                                    blank=True,null=True)
    aggrement_date = models.DateField()
    company_location = models.CharField(
                                    max_length=50,
                                    verbose_name=_("Location"),
                                    blank=True, null=True,
                                    help_text=_("Company Addres location-upto 50 chars"))
    company_street = models.CharField(
                                    max_length=50,
                                    verbose_name=_("Street"), 
                                    blank=True, null=True,
                                    help_text=_("Company Addres street-upto 50 chars"))
    company_city = models.CharField(
                                    max_length=150,
                                    verbose_name=_("Company City"), 
                                    blank=True, null=True,
                                    help_text=_("Company Addres city-upto 50 chars"))    
    company_state = models.CharField(
                                    max_length=50,
                                    verbose_name=_("state"),
                                    blank=True, null=True,
                                    help_text=_("Company Addres state-upto 50 chars")) 
    company_country = models.CharField(
                                    max_length=50, 
                                    verbose_name=_("Country"), 
                                    blank=True,null=True,
                                    help_text=_("Company Addres Country-upto 50 chars"))
    company_pincode = models.CharField(
                                    max_length=6,
                                    verbose_name=_("Pincode"), 
                                    blank=True, null=True,
                                    help_text=_("Company Addres pincode-upto 6 chars"))    
    onsite_deliver = models.BooleanField(
                                    default=True, 
                                    verbose_name=_("Onsite Deliver"))
    num_employess = models.CharField(
                                    max_length=2,
                                    verbose_name=_("Number of Employees"),
                                    blank=True,null=True,
                                    help_text=_("Our emplooyes number with customer"))
    employees = models.ManyToManyField(
                                    Employee,
                                    verbose_name=_("Employees"),
                                    help_text=_("Employess working with customer"))
    emp_department = models.CharField(
                                    max_length=150,
                                    verbose_name=_("Employee Wroking Department"),
                                    blank=True,null=True)   
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.company_name
    
    def get_company_name(self):
        """
            returns company name
        """
        if self.company_name:
            return self.company_name
        else:
            return "n/a"
    
    def get_contact_email(self):
        """
            returns contact email
        """
        if self.contact_email:
            return self.contact_email
        else:
            return "n/a"
        
    def get_contact_number(self):
        """
            returns contact number
        """
        if self.contact_number:
            return self.contact_number
        else:
            return "n/a"
    
    def get_company_address(self):
        """
            returns company full address
        """
        if self.company_name & self.company_city & \
            self.company_location & self.company_street & \
            self.company_state and self.company_country:
            return "{}\n{}\n{}\n{}\n{}\n{}".format(self.company_name & self.company_city & \
                                            self.company_location & self.company_street & \
                                            self.company_state and self.company_country)
        else:
            return "n/a"
    
    def validate_unique(self, *args, **kwargs):
        super(Customer, self).validate_unique(*args, **kwargs)
        
        email_qs = self.__class__.default_manager.filter(
            Q(contact_email=self.contact_email)|Q(contact_email=self.alt_email)        
        )
        number_qs = self.__class__.default_manager.filter(
            Q(contact_number=self.contact_number)|Q(contact_number=self.alt_number)        
        )
        
        if email_qs.exists():
            raise ValidationError({
               'Pleave Provide valid email id, contact email and alternative email should not be same'
            })
        
        if number_qs.exists():
            raise ValidationError({
                   "Pleave Provide valid contact number, contact number and alternative number should not be same"
            })
    
    def clean(self, *args, **kwargs):
        """
            validate column types and change to lower case before saving
        """
        if self.company_name:
            self.company_name = self.company_name.lower()
        if self.company_type:
            self.company_type = self.company_type.lower()
        if self.company_domain:
            self.company_domain = self.company_domain.lower()
        if self.contact_person:
            self.contact_person = self.contact_person.lower()
        if self.contact_email:
            self.contact_email = self.contact.email.lower()
        if self.company_location:
            self.company_location = self.company_location.lower()
        if self.company_street:
            self.company_street = self.company_street.lower()
        if self.company_city:
            self.company_city = self.company_city.lower()
        if self.company_state:
            self.company_state  = self.company_state.lower()
        if self.company_country:
            self.company_country = self.company_country.lower()
        super(Customer, self).clean(*args, **kwargs)
    
    def save(self, *args,**kwargs):
        """
            saving current instance model
        """
        self.full_clean()
        super(Customer, self).save(*args, **kwargs)
   
    
                                          