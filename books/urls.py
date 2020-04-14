from django.urls import path
from django.contrib import admin
from .views import home_view

app_name = 'books'

urlpatterns = [    
    path('', home_view, name='header'),
]
