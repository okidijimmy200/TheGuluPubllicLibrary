from django.urls import path
from django.contrib import admin
from .views import home_view, all_books, detail_view

app_name = 'books'

urlpatterns = [    
    path('', home_view, name='main'),
    path('list', all_books, name='all_books'),
    path('<slug:book>/', detail_view, name='detail_view')
   
]
