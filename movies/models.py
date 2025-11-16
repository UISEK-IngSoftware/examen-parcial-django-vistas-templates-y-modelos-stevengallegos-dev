from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)                
    release_year = models.PositiveIntegerField()            
    director_name = models.CharField(max_length=100)      
    genre = models.CharField(max_length=50)                
    synopsis = models.TextField()                          


    def __str__(self):
        return self.title
