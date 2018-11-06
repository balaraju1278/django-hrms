"""
    Author: Bala
    Description: customer project models lives here
"""
from django.db import models 
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError, models, transaction
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
                                verbose_name=_("Project Title"), 
                                help_text=_("Customer Project title"))
    description = models.TextField(
                                verbose_name=_("Description"), 
                                help_text=_("Small Description about customer project"), 
                                blank=True, null=True)
    employees = models.ManyToManyField(
                                Employee, verbose_name=_("Employees"),
                                related_name='employees_with_customer', 
                                help_text=_("Employess working with Customer"))    
    project_head = models.CharField(
                                max_length=100, 
                                verbose_name=_("Project Head"), 
                                help_text=_("Project Head[customer side]"), 
                                blank=True, null=True)
    project_dealer = models.ForeignKey(
                                Employee,related_name='account_manager_with_customer', 
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
    slug = models.SlugField(verbose_name=_('Slug'), unique=True, max_length=100)


    def __repr__(self):
        return '%s' % (self.title)
    
    def __str__(self):
        return '%s' % (self.title)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self._meta.concrete_model != other._meta.concrete_model:
            return False
        c_pk = self.pk
        if c_pk is None:
            return self is other
        return c_pk == other.pk
    
    def __gt__(self, other):
        return '%s' %(self.__class__.__name__.lower() > other.name.lower())
    
    def __lt__(self, other):
        return '%s' %(self.__class__.name__.lower() < other.name.lower())

    def __hash__(self):
        if self.pk is None:
            raise TypeError("Model instances without primary key value are unhashable")
        return hash(self.pk)
    
    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            self.slug = self.slugify(self.title)
            from django.db import router
            using = kwargs.get("using") or router.db_for_write(
                    type(self), instance=self)
            kwargs["using"] = using
            try:
                with transaction.atomic(using=using):
                    res = super(self.__class__, self).save(*args, **kwargs)
                return res
            except IntegrityError:
                pass
            c_slugs = set(
                    self.__class__._default_manager.filter(
                                    slug__startswith=self.slug)
                                    .values_list('slug',flat=True)            
            )
            i = 1
            while True:
                slug = self.slugify(self.comapany_name, i)
                if slug not in c_slugs:
                    self.slug = slug
                    # We purposely ignore concurrecny issues here for now.
                    # (That is, till we found a nice solution...)
                    return super(self.__class__, self).save(*args, **kwargs)
                i += 1
        else:
            return super(self.__class__, self).save(*args, **kwargs)
            
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
            self.project_head = self.project_head.lower()
        super(CustomerProject,self).clean(*args, **kwargs)
        

    class Meta:
        verbose_name = _("Customer Projects")
        verbose_name_plural = _("Customer Projects")        