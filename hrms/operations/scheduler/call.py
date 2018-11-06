"""
    author : Bala
    call models[Base Call, Investor Call, Customer Call, Interview Call] are lives here
    don't add fetures in Base Call class try to add in Extended Class
"""

import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
    ValidationError    
    )

from django.utils.translation import ugettext as _
from operations.utils.status import CALL_STATUS
from .base import Person
from people.models import Employee

class Call(models.Model):
    """
        base call model
    """
    employee = models.ForeignKey(
                Employee, 
                verbose_name=_("Employee"),
                blank=True, null=True)
    description = models.TextField( 
                verbose_name=_("Description"), 
                blank=True, null=True)
    date_of_creation = models.DateTimeField(
                verbose_name=_("Created at"), 
                auto_now_add=True)
    date_due = models.DateTimeField()
    last_modification = models.DateTimeField(
                verbose_name=_("Last Modified"),
                auto_now=True)
    status = models.CharField(
                max_length=15,
                verbose_name=_("Status"), 
                blank=True, null=True, 
                choices=CALL_STATUS)
    result_note = models.TextField(
                verbose_name=_("Result Summary"),
                 blank=True, null=True)
    
    def save_description(self, *args, **kwargs):
        self.description = self.description.lower()
        super(Call, self).save(*args, **kwargs)
    
    def save_status(self, *args, **kwargs):
        self.status = self.status.lower()
        super(Call, self).save(*args, **kwargs)
        
    def get_employee(self):
        """
            returns employee to call
        """
        if self.employee:
            return str(self.employee)
        else:
            return "n/a"
    
    def get_status(self):
        """
            returns call status
        """
        if self.status:
            return self.status
        else:
            return "n/a"
    
    def get_duration(self):
        """
            returns call duration from to to
        """
        if self.date_of_creation & self.date_due:
            return self.date_of_creation.strftime('%d, %b, %Y')\
            + '==>' +self.date_due.strftime("%d, %b, %Y")
        else:
            return "n/a"
            
    def __str__(self):
        return _("Call")+ ' ' +str(self.id)
    
    
class InvestorCall(Call, Person):
    
    def __str__(self):
        return self.employee + "===>" + self.name
    
    def validate_unique(self, *args, **kwargs):
        super(InvestorCall, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__._default_manager.filter(
            date_of_creation__lt=self.date_due,
            date_due__gt=self.date_of_creation
        )
        
        if not self._state.adding and self.pk is not None:
            qs = qs.exclude(pk=self.pk)
        
        if qs.exists():
            raise ValidationError(
                'overlapping date range'
            )
        
    def clean(self, *args, **kwargs):
        if self.name:
            self.name = self.name
        if self.pref_name:
            self.pref_name = self.pref_name.lower()
        if self.email:
            self.email = self.email.lower()
        if self.role:
            self.role = self.role.lower()
        if self.company:
            self.company = self.company.lower()
        if self.description:
            self.description = self.description.lower()
        if self.result_node:
            self.result_note = self.result_note.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(InvestorCall, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Investor Calls'
        verbose_name_plural = 'Investor Calls'


class InterviewCall(Call, Person):
    call_for_role = models.CharField(
                    max_length=20, 
                    verbose_name=_("Interview Postion"), 
                    blank=True, null=True)
    
    def __str__(self):
        return self.employee + '===>' + self.name
    
    
    def validate_unique(self, *args, **kwargs):
        super(InvestorCall, self).validate_unique(*args, **kwargs)
        
        email_qs = self.__class__._default_manager.filter(
            email=self.email        
        )
        number_qs = self.__class__._default_manager.filter(
            phone_number=self.phone_number        
        )
        qs = self.__class__._default_manager.filter(
            date_of_creation__lt=self.date_due,
            date_due__gt=self.date_of_creation
        )
        
        if not self._state.adding and self.pk is not None:
            qs = qs.exclude(pk=self.pk)
        
        if qs.exists():
            raise ValidationError(
                'overlapping date range'
            )
        if email_qs.exists():
            raise ValidationError("Already Interviewd this candidate")
        
        if number_qs.exists():
            raise ValidationError("Already Interviewd this candidate")
        
    def clean(self, *args, **kwargs):
        if self.name:
            self.name = self.name
        if self.pref_name:
            self.pref_name = self.pref_name.lower()
        if self.email:
            self.email = self.email.lower()
        if self.role:
            self.role = self.role.lower()
        if self.company:
            self.company = self.company.lower()
        if self.description:
            self.description = self.description.lower()
        if self.result_node:
            self.result_note = self.result_note.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(InvestorCall, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _('Interview Calls')
        verbose_name_plural = _('Interview Calls')


class CustomerCall(Call, Person):
    
    def __str__(self):
        return self.employee + '===>' + self.name
    
    def validate_unique(self, *args, **kwargs):
        super(InvestorCall, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__._default_manager.filter(
            date_of_creation__lt=self.date_due,
            date_due__gt=self.date_of_creation
        )
        
        if not self._state.adding and self.pk is not None:
            qs = qs.exclude(pk=self.pk)
        
        if qs.exists():
            raise ValidationError(
                'overlapping date range'
            )

        
    def clean(self, *args, **kwargs):
        if self.name:
            self.name = self.name
        if self.pref_name:
            self.pref_name = self.pref_name.lower()
        if self.email:
            self.email = self.email.lower()
        if self.role:
            self.role = self.role.lower()
        if self.company:
            self.company = self.company.lower()
        if self.description:
            self.description = self.description.lower()
        if self.result_node:
            self.result_note = self.result_note.lower()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(InvestorCall, self).save(*args, **kwargs)
    class Meta:
        verbose_name = _("Customer Calls")
        verbose_name_plural = _("Customer Calls")


class CallOverDueFilter(admin.SimpleListFilter):
    title = _("Is call overdue")
    parameter_name = 'date_due'
    
    def lookups(self, request, model_admin):
        return (
            ('overdue', _('OverDue')),
            ('planned', _('Planned')),        
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'planned':
            return queryset.fitler(date_due__get=timezone.now())
        elif self.value() == 'overdue':
            return queryset.filter(
                    date_due__lt=timezone.now().exclude(status__in=['F', 'S']))
        else:
            return queryset


class OptionCall(admin.ModelAdmin):
    list_display = ('id',
                    'description',
                    'date_due',
                    'purpose',
                    'status',
                    'cperson',
                    'is_call_overdue',
                    'get_contact_name')
    fieldsets = (('', {'fields': ('staff',
                                  'description',
                                  'date_due',
                                  'purpose',
                                  'company',
                                  'cperson',
                                  'status')}),)
    list_filter = [CallOverDueFilter]
    
    @staticmethod
    def get_contact_name(obj):
        return obj.company.name
    
    get_contact_name.short_description = _("Company")
    
    @staticmethod
    def is_call_overdue(obj):
        if obj.date_due < timezone.now() and obj.status not in ['F', 'S']:
            overdue = True
        else:
            overdue = False
        return overdue
        
    is_call_overdue.short_description = _("Is call overdue")