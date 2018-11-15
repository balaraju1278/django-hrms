from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError
from django.conf import settings


class BooksCategory(models.Model):
    _type = models.CharField(max_length=100) 
    
    def get__type(self):
        return self._type
    
    def __str__(self):
        return self.get__type
    
    def __repr__(self):
        return self.get__type
    
    def _get_books(self):
        return ', '.join(self.book_types.all().values_list('name', flat=True))
    
    def validate_unique(self, *args, **kwargs):
        super(BooksCategory, self).validate_unique(*args, **kwargs)
        qs = self.__class__._default_manager.filter(_type=self._type).exists()
        if qs:
            raise ValidationError("Category already exists")
    
    def clean(self, *args, **kwargs):
        if self._type:
            self._type = self._type.lower()
    
    class Meta:
        verbose_name = _("Book Category")
        verbose_name_plural = _("Book Categories")
        
    
class Book(models.Model):
    BOOK_TYPE_CHOICES = (
    
    )
    name = models.CharField(max_length=300)
    isbn_number = models.CharField(max_length=15)
    language = models.CharField(max_length=100)
    programing_language = models.CharField(max_length=40)
    book_type = models.ForeignKey(
                BooksCategory, related_name="book_types",
                on_delete=models.CASCADE, 
                verbose_name=_("book_types"))
    file = models.FileField(upload_to='resources/books/')
    
    class Meta:
        db_table = 'books'
        verbose_name = _("Books")
        verbose_name_plural = _("Books")
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
        
    def get_name(self):
        if self.name:
            return self.name
        else:
            return "n/a"
            
    def get_language(self):
        if self.language:
            return self.language
        else:
            return "n/a"
            
    def get_programing_language(self):
        if self.programing_language:
            return self.programing_language
        else:
            return "n/a"
            
    def book_type(self):
        if self.book_type:
            return self.book_type
        else:
            return "n/a"
    
    def get_authors(self):
        return ', '.join(self.authors.all().values_list('name', flat=True))
    
    def get_language_descendants(self):
        lg_books = self.__class__._default_manager.filter(language=self.get_language)
        return lg_books
    
    def get_program_descendants(self):
        pg_books = self.__class__._default_manager.filter(programing_language=self.get_programing_language)
        return pg_books
    
    def get_book_type_descendants(self):
        bt_books = self.__class__._default_manager.filter(book_type=self.book_type)
        return bt_books
        
    def validate_unique(self, *args, **kwargs):
        super(Book, self).validate_unique(*args, **kwargs)
        qs = self.__class__._default_manager.filter(
            name=self.name        
        )
        if qs.exists():
            raise ValidationError("Book already exists with same name")
    
    def clean(self, *args, **kwargs):
        if self.name:
            self.name = self.name.lower()
        if self.isbn_number:
            self.isbn_number = self.isbn_number.lower()
        if self.language:
            self.language = self.language.lower()
        if self.programing_language:
            self.programing_language = self.programing_language.lower
            
            
class Author(models.Model):
    name = models.CharField(max_length=300)
    book = models.ForeignKey(Book, related_name='authors', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'author'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

        
class Reader(models.Model):
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}==.{}'.format(self.book, self.reader)
    
    def __repr__(self):
        return '{}==.{}'.format(self.book, self.reader)


class BComment(models.Model):
    book = models.ForeignKey(Book, related_name='comments')
    commentor = models.ForeignKey(settings.AUTH_USER_MODEL)
    commented_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
    def get_text(self):
        return self.text
    