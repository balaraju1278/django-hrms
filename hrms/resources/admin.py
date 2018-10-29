from django.contrib import admin
from .models import Book, Video, Blog, Other
# Register your models here.

admin.site.register(Book)
admin.site.register(Video)
admin.site.register(Blog)
admin.site.register(Other)