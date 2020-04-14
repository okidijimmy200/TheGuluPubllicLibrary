from django.db import models

# Create your models here.
# model for class
class Book(models.Model):

    def __str__(self):

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
        