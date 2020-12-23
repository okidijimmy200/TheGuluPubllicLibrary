from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'author', 'genre', 'timestamp', 'body')
    list_filter = ('genre', 'name')
    search_filter = ('name', 'body')
    prepopulated_fields={'slug':('name',)}    
    ordering = ('genre', 'timestamp')
