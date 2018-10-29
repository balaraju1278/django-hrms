from django.db import models
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
    ValidationError    
    )
from django.utils.translation import ugettext as _
from operations.utils.postalaaddressprefix import POSTALADDRESSPREFIX


class PhoneAddress(models.Model):
    """
        extra utility phone address for future use
    """
    phone = models.CharField(
            max_length=15, 
            verbose_name=_("Phone Number"))
    
    def __str__(self):
        return self.phone
    
    def validate_unique(self, *args, **kwargs):
        super(PhoneAddress, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__.default_manager.filter(
            phone=self.phone        
        )
        if qs.exists():
            raise ValidationError("Duplicate Phone Address")
            
    def clean(self, *args, **kwargs):
        if self.phone:
            self.phone=self.phone.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(PhoneAddress, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _("Phone Address")
        verbose_name_plural = _("Phone Address")
        

class EmailAddress(models.Model):
    """
        extra utility email address for future use
    """
    email = models.EmailField(
            max_length=200, 
            verbose_name=_("Email Address"))
    
    def __str__(self):
        return self.email
    
    def validate_unique(self, *args, **kwargs):
        super(EmailAddress, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__.default_manager.filter(
            email=self.email        
        )
        if qs.exists():
            raise ValidationError("Duplicate Email ID")
            
    def clean(self, *args, **kwargs):
        if self.email:
            self.email=self.email.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(EmailAddress, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Email Address")
        verbose_name_plural = _("Email Address")
     

class Person(models.Model):
    """
        Very base person model which will be latter extends for visits, calls
    """
    prefix = models.CharField(
                max_length=4, 
                choices=POSTALADDRESSPREFIX, 
                verbose_name=_("Prefix"), 
                blank=True, null=True )
    name = models.CharField(
                max_length=100, 
                verbose_name=_("Name"), 
                blank=True, null=True)
    pref_name = models.CharField(
                max_length=100, unique=True,
                verbose_name=_("Pref Name"),  
                blank=True, null=True)
    email = models.EmailField(
                max_length=200,unique=True, 
                verbose_name=_("Email Address"))
    phone_number = models.CharField(
                max_length=15, unique=True,
                verbose_name=_("Phone Number"))
    role = models.CharField(
                max_length=40, 
                verbose_name=_("Role"), 
                blank=True, null=True)
    company = models.CharField(
                max_length=100, 
                verbose_name=_("Company Name"), 
                blank=True)
    
    def save_name(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Person, self).save(*args, **kwargs)
    
    def save_pref_name(self, *args, **kwargs):
        self.pref_name = self.pref_name.lower()
        super(Person, self).save(*args, **kwargs)
    
    def save_email(self, *args, **kwargs):
        self.email = self.email.lower()
        super(Person, self).save(*args, **kwargs)
    
    def save_role(self, *args, **kwargs):
        self.role = self.role.lower()
        super(Person, self).save(*args, **kwargs)
    
    def save_company(self, *args, **kwargs):
        self.company = self.company.lower()
        super(Person, self).save(*args, **kwargs)
        
    def get_pref_name(self):
        """
            returns pref name
        """
        if self.pref_name:
            return self.pref_name
        else:
            return "n/a"
    
    def get_name(self):
        """
            returns name 
        """
        if self.name:
            return self.name
        else:
            return "n/a"
    
    def get_email(self):
        """
            returns email
        """
        if self.email:
            return self.email
        else:
            return "n/a"
    
    def get_phone_number(self):
        """
            returns phone number
        """
        if self.phone_number:
            return self.phone_number
        else:
            return "n/a"
            
    def __str__(self):
        """
            string reporesentaion of instance
        """
        return self.get_pref_name() + ' ' + self.get_name()+ ' ' + self.get_email()
    
    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Person")
        abstract = True