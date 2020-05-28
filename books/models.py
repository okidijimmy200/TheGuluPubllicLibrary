import random
from django.conf import settings
import os
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q


'''HOW FILE SYSTEM, IMAGE EXTENSION WORK
https://www.geeksforgeeks.org/imagefield-django-models/
'''


#getting filename extension
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext  


# function for imagefield
def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1000000000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext=ext)
    return "media/{new_filename}/{final_filename}".format(new_filename=new_filename, filename=final_filename )


# book query set
class BookQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = Q(name__icontains=query)|Q(author__icontains=query)
        return self.filter(lookups).distinct()

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db )

    def search(self, query):
        return self.get_queryset().search(query)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() ==1:
            return qs.first()
        return None

class Book(models.Model):

    GENRE = (
        ('S', 'Science Fiction'),
        ('D', 'Drama'),
        ('H', 'History'),
        ('C', 'Crime')
    )
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=1, choices=GENRE)
    timestamp =  models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250,
                        unique_for_date='timestamp')
    upload = models.ImageField(upload_to='media/', null=True, blank=True)
    body = models.TextField(max_length=500)

    class Meta:
        ordering = ["-timestamp",]
        
    
    def __str__(self):
        return self.name

    objects = models.Manager()
    objects = BookManager()
# finding the absolute url
    def get_absolute_url(self):
        return reverse('books:detail_view',
                        args=[self.slug])

    

    

    