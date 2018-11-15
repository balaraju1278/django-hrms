from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError
from django.conf import settings


class VideosCategory(models.Model):
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
        super(VideosCategory, self).validate_unique(*args, **kwargs)
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
    video_type = models.ForeignKey(VideosCategory, on_delete=models.CASCADE,related_name="videos")
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
    
    def get_type_descendants(self):
        videos = self.__class__._default_manager.filter(video_type=self.video_type)
        return videos
    
    def validate_unique(self, *args, **kwargs):
        super(Video, self).validate_unique(*args, **kwargs)
        qs = self.__class__._default_manager.filter(_title=self._title).exists()
        if qs:
            raise ValidationError("Duplicate Title")
    
    def clean(self):
        if self._title:
            self._title = self._title.lower()
        if self._desc:
            self._desc = self._desc.lower()


class Viewer(models.Model):
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="viewers")
    video = models.ForeignKey(Video, related_name='videos')
    
    def __str__(self):
        return "{}==>{}".format(self.viewer, self.video)
    
    def __repr__(self):
        return "{}==>{}".format(self.viewer, self.video)


class VComment(models.Model):
    video = models.ForeignKey(Video, related_name="comments")
    commentor = models.ForeignKey(settings.AUTH_USER_MODEL)
    commented_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    def get_text(self):
        return self.text