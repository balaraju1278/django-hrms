from django.db import models

# Create your models here.

class Book(models.Model):
    class Meta:
        verbose_name = "Book"


class Video(models.Model):
    class Meta:
        verbose_name = "Video"


class Blog(models.Model):
    class Meta:
        verbose_name = "Blog"


class Other(models.Model):
    class Meta:
        verbose_name = "Other"