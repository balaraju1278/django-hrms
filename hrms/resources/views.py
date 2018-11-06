from django.shortcuts import render
from django.shortucts import render, redirect
from django.views import generic

from .forms import BookFormset, BookModelFormset, BookModelForm, AuthorFormset
from .models import Book, Author
# Create your views here.


def add_book(request):
    template_name = 'add_book.html'
    heading_message = 'Adding Book to Reources'
    
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                if name:
                    Book(name=name).save()
            return redirect('resources:book_list')
    
    return render(request, template_name, {'formset': formset, 'heading':heading_message,})


class BookListView(generic.ListView):
    model = Book
    contact_object_name = 'books'
    template_name = 'books_list.html'
    

def add_book_model_form(request):
    template_name = 'add_book.html'
    heading_message = 'Adding Book to Resources'
    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('books_list')
    return render(request, template_name, {'formset':formset, 'heading':heading_message,})
    


def add_book_with_authors(request):
    template_name = 'add_book_with_author.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            book = bookform.save()
            for form in formset:
                author = form.save(commit=False)
                author.book = book
                author.save()
            return redirect('booklist')
    return render(request, template_name, {'bookform': bookform, 'formset': formset})