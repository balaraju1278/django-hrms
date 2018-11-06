from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError


class Category(models.Model):
    _type = models.CharField(max_length=100) 
    
    def get__type(self):
        return self._type
    
    def __str__(self):
        return self.get__type
    
    def __repr__(self):
        return self.get__type
    
    def _get_videos(self):
        return ', '.join(self.videos.all().values_list('name', flat=True))
    
    def validate_unique(self, *args, **kwargs):
        super(Category, self).validate_unique(*args, **kwargs)
        qs = self.__class__._default_manager.filter(_type=self._type).exists()
        if qs:
            raise ValidationError("Category already exists")
    
    def clean(self, *args, **kwargs):
        if self._type:
            self._type = self._type.lower()
    
    class Meta:
        verbose_name = _("Video Category")
        verbose_name_plural = _("Video Categories")


class Video(models.Model):
    _title = models.CharField(max_length=150)
    _desc = models.CharField(max_length=500)
    video_type = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="videos")
    video_url = models.CharField(max_length=400)
    
    def get__title(self):
        if self._title:
            return self._title
        else:
            return "n/a"
    
    def get__desc(self):
        if self._desc:
            return self._desc
        else:
            return "n/a"
        
    def get_video_type(self):
        if self._video_type:
            return self._video_type
        else:
            return "n/a"
    
    def video_url(self):
        if self._video_url:
            return self._video_url
        else:
            return "n/a"