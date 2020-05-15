from django.shortcuts import render
from .models import Book


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

