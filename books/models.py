from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

'''HOW FILE SYSTEM, IMAGE EXTENSION WORK
https://www.geeksforgeeks.org/imagefield-django-models/
'''

# location where image will be stored
fs = FileSystemStorage(location='/media/photos')


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
    upload = models.ImageField(storage=fs, null=True, blank=True) 
    body = models.TextField()

    class Meta:
        ordering = ["-timestamp",]
        
    
    def __str__(self):
        return self.name

    objects = models.Manager()

   

    

    

    