"""
    Author: Bala
    Description: Task Base models utils lives here
    models: BaseTask
"""

# django core imports
from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError



class BaseTask(models.Model):
    """
        base task model
    """
    HIGH = 'H'
    LOW = 'L'
    NORMAL = 'N'
    
    PRIORITY_CHOICES = (
        ('H', 'HIGH'),
        ('L', 'LOW'),
        ('N', 'NORMAL'),    
    )
    
    TASK_STATUS = (
        ('C', 'COMPLETED'),
        ('ON', 'ONGOING'),
        ('R', 'UNDER REVIEW')    
    )
    
    RESULT_STATUS = (
        ('A', 'APPROVED'),
        ('R', 'REJECTED'),    
    )
    
    title = models.CharField(
                            max_length=150, 
                            verbose_name=_("Title"), 
                            blank=True, null=True)
    description = models.TextField(
                            verbose_name=_("Description"), 
                            blank=True, null=True)
    priority = models.CharField(
                            max_length=6, 
                            verbose_name=_("Priority"), 
                            blank=True, null=True)    
    created_at = models.DateTimeField(
                            auto_now_add=True,
                            verbose_name=_("Created At"), 
                            blank=True, null=True)
    due_date = models.DateField(
                            verbose_name=_("Due Date"), 
                            blank=True, null=True)
    
    current_status = models.CharField(
                            verbose_name=_("Current Status"), 
                            blank=True, null=True, 
                            max_length=10)
    result_status = models.CharField(
                            verbose_name=_("Result Status"), 
                            blank=True, null=True, 
                            max_length=10)
         
    def __str__(self):
        return self.title
    
    def get_priority_descendents(self):
        """
            return curent instance model like priority objects
        """
        pri_descs = self.__class__.objects.filter(priority=self.priority)
        return pri_descs
        
    @property
    def get_title(self):
        """
            returns title of task
        """
        if self.title:
            return self.title
        else:
            return "n/a"
    
    @property
    def get_due_date(self):
        """
            returns due date of task
        """
        if self.due_date:
            return self.due_date.strftime("%d, %b, %Y")
        else:
            return "n/a"
    
    @property
    def ger_remaining_days(self):
        """
            returns remaing days of task
        """
        if self.created_at & self.due_date:
            c_date = self.created_at
            d_date = self.due_date
            rm_days = d_date-c_date
            return rm_days.strftime("%d, %b, %Y")
        else:
            return "This task is TBD"
    
    @property
    def get_current_status(self):
        """
            returns current status of task
        """
        if self.current_status:
            return self.current_status
        else:
            return "n/a"
    
    @property
    def get_result_status(self):
        """
            returns result status of task
        """
        if self.result_status:
            return self.result_status
        else:
            return "n/a"
            
    def validate_unique(self, *args, **kwargs):
        """
            validate unique title
        """
        super(self.__class__, self).validate_unique(*args, **kwargs)
        
        qs = self.__class__.objects.filter(title=self.title)
        if qs:
            raise ValidationError("Duplicate title")
    
    def clean(self, *args, **kwargs):
        """
            type validation and change to lower case
        """
        if self.title:
            self.title = self.title.lower()
        if self.description:
            self.description = self.description.lower()
        if self.priority:
            self.priority = self.priority.lower()
        if self.current_status:
            self.current_status = self.current_status.lower()
        if self.result_status:
            self.result_status = self.result_status.lower()
    
    def save(self, *args, **kwargs):
        """
            calling full_clean
        """
        super(self.__class__, self).save(*args, **kwargs)
        
    class Meta:
        app_label = _("tasks")
        db_table = _("base_task")
        ordering = ("title",)        
        verbose_name = _("Base Tasks")
        verbose_name_plural = _("Base Tasks")
    

class TaskAttachmentFile(models.Model):
    attachment = models.FileField(
                                    upload_to='tasks/', 
                                    blank=True, null=True, 
                                    verbose_name=_("Attachement File"), 
                                    help_text=_("attach any refference file for task"))
    class Meta:
        verbose_name = _("Task Attachement File")