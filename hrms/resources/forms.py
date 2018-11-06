from django import forms
from django.forms import formset_factory, modelformset_factory
from .r_models.books import Book, Author



class BookForm(forms.Form):
    name = forms.CharField(
            label='Book Name',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name Here'
            })
    )
    isbn_number = forms.CharField(
            label='ISBN Number',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter isbn number Here'
            })
    )
    language = forms.CharField(
            label='Language',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Language of book'
            })
    )
    programing_language = forms.CharField(
            label='Programing Language',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Progaming Language of book'
            })
    )
    book_type = forms.CharField(
            label='Book Type',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            })
    )
    file = forms.FileField(
            label='Book Type',
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            })    
    )
    
    
class BookModelForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('name', 'isbn_number', 'language', 'progaming_language', 'book_type', 'file')
        labels = {
            'name': 'Book Name',
            'isbn_number': 'Enter ISBN Number',
            'language': 'Book in Language',
            'programing_language': 'Programing Language',
            'book_type': 'Book Type',
            'file': 'Book'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
            }),
            'isbn_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placholder': 'Enter ISBN number if available'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Language of book'
            }),
            'programing_language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Programing Language ex: data science, sales'
            }),
            'book_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Book Type ex:Motivational, programming ..etc'
            }),
            'file': forms.FileField(attrs={
                'class': 'form-control',
                'placeholder' : 'select book file'
            })
                    
        }
        
    def clean_name(self):
        name_inst = self.cleaned_data.get('name')
        validate = self.__class__.meta.model._default_manager.filter(name=name_inst).exists()
        if validate:
            raise forms.ValidationError(self.validation_messages.get('name'))
        return name_inst
    
    def clean_isbn_number(self):
        isbn_inst = self.cleaned_data.get('isbn_number')
        validate = self.__class__.meta.model._default_manager.filter(isbn_number=isbn_inst).exists()
        if validate:
            raise forms.ValidationError(self.validation_messages.get('isbn'))
        return isbn_inst


BookFormset = formset_factory(BookForm)
BookModelFormset = modelformset_factory(
    Book, fields=('name','isbn_number', 'language', 'programing_language', 'book_type', 'file' ),
    extra=1,
    widgets={
          'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
            }),
            'isbn_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placholder': 'Enter ISBN number if available'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Language of book'
            }),
            'programing_language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Programing Language ex: data science, sales'
            }),
            'book_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Book Type ex:Motivational, programming ..etc'
            }),
            'file': forms.FileField(attrs={
                'class': 'form-control',
                'placeholder' : 'select book file'
            }) 
    }
)

AuthorFormset = modelformset_factory(
    Author, fields=('name', ),
    extra=1,
    widgets={
         'name':forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name Here'
         })   
    }
    
)