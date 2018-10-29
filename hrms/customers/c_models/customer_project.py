"""
    Author: Bala
    Description: customer project models lives here
"""
from django.db import models 
from django.utils.translation import ugettext as _
from django.utils.translation import ugettextlazy as _

from .customer import Customer
from people.models import Employee



class CustomerProject(models.Model):
    """
        customer project model
    """
    PROJECT_STATUS = (
        ('Started', 'STARTED'),
        ('ON_GOING', 'ON_GOING'),
        ('COMPLETD', 'COMPLETED'),    
    )
    customer = models.ForeignKey(
                                Customer,verbose_name=_("Customer"),
                                on_delete=models.CASCADE)    
    title = models.CharField(
                                max_length=300, 
                                blank=True, null=True, 
                                varbose_name=_("Project Title"), 
                                help_text=_("Customer Project title"))
    description = models.TextField(
                                verbose_name=_("Description"), 
                                help_text=_("Small Description about customer project"), 
                                blank=True, null=True)
    employees = models.ManyToManyField(
                                Employee, verbose_name=_("Employees"), 
                                help_text=_("Employess working with Customer"))    
    project_head = models.CharField(
                                max_length=100, 
                                verbose_name=_("Project Head"), 
                                help_text=_("Project Head[customer side]"), 
                                blank=True, null=True)
    project_dealer = models.ForeignKey(
                                Employee, 
                                verbose_name=("Account Manager"), 
                                help_text=_("Contact Account Manager"),
                                on_delete=models.CASCADE)
    status = models.CharField(
                                max_length=10, 
                                verbose_name=_("Projec Status"), 
                                choices=PROJECT_STATUS)
    started_at = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    modefied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_title(self):
        """
            returns project title
        """
        if self.title:
            return self.title
        else:
            return "n/a"
    
    def get_project_dealer(self):
        """
            returns project account manager
        """
        if self.project_dealer:
            return self.project_dealer
        else:
            return "n/a"
    
    def clean(self, *args, **kwargs):
        """
            validating column types and saving  into lower case 
        """
        if self.title:
            self.title = self.title.lower()
        if self.description:
            self.description = self.description.lower()
        if self.project_head:
            self.project_head = self.project_head()
        super(CustomerProject,self).clean(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        """
            saving current instance of customer project
        """
        self.full_clean()
        super(Customer, self).save(*args, **kwargs)
    class Meta:
        verbose_name = _("Customer Projects")
        verbose_name_plural = _("Customer Projects")        