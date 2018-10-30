"""
    Author: Bala
    description: Development task models lives here
"""

# django core imports
from django.db import models
from django.utils.translation import ugettext as _

# local file/modules imports
from .base import BaseTask, TaskAttachmentFile
from people.models import Employee



class DevelopmentTask(BaseTask):
    """
        development task model
    """
    employees = models.ManyToManyField(
                            Employee,
                            related_name="emplooyes",
                            verbose_name=_("Employees"))
    review_by = models.ForeignKey(
                            Employee, 
                            related_name="reviewer",
                            verbose_name=_("Review By"))    
    send_copy_email = models.BooleanField(default=True)
    instructions = models.TextField(
                            verbose_name=_("Instructions"), 
                            blank=True, null=True,
                            help_text=_("Instructions/guidelines for task"))
    attachment = models.ForeignKey(
                                    TaskAttachmentFile,
                                   verbose_name=_("Attchement"))


        
    def __str__(self):
        return self.title
    
    def get_tasks_of_reviewer(self):
        """
            returns total tasks of current instance reviewer
        """
        reviewer_tasks = self.__class__.objects.filter(review_by=self.review_by)
        return reviewer_tasks
        
    @property
    def get_status(self):
        """
            returns task status
        """
        if self.status:
            return self.status
        else:
            return "n/a"
    
    def clean(self, *args, **kwrgs):
        """
            validates type and convert to lower case
        """
        if self.instructions:
            self.instructions = self.instructions.lower()
    
    def save(self, *args, **kwargs):
        """
            saving to db and sending an email copy to
            emplooys and reviewer
        """
        # impliment send a copy mail to employees and reviewer
        super(self.__class__, self).save(*args, **kwargs)
        
    
    class Meta:
        
        verbose_name = _("Development Task")
        verbose_name_plural = _("Development Tasks")


