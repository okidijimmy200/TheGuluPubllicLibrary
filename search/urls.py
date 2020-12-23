from django.urls import path
from django.contrib import admin
from .views import SearchView

app_name = 'search'

urlpatterns = [    
    path('result', SearchView.as_view(), name='query'),
    
]