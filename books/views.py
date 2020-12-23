from django.shortcuts import render,  get_object_or_404
from .models import Book
from django.http import Http404
from django.views import generic

def home_view(request):
    books = Book.objects.all()[:3]
    context = {"books":books}
    template = "books/main.html"
    return render(request, template, context)

# view for allBooks
def all_books(request):
    all_books = Book.objects.all()
    context = {"all_books":all_books}
    template = "books/allBooks.html"
    return render(request, template, context)


   
def detail_view(request, book):
    book = get_object_or_404(Book, slug=book)

    return render(request, "books/detail.html",
                {'book':book} )

    
