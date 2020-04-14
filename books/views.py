from django.shortcuts import render
from .models import Book


def home_view(request):
    books = Book.objects.all()
    context = {"books":books}
    template = "books/header.html"
    return render(request, template, context)


