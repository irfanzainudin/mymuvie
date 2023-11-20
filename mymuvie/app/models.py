import datetime
from django.db import models


class Movie(models.Model):
    title = models.TextField()
    year = models.CharField(max_length=10)
    rated = models.CharField(max_length=10, null=True)
    released = models.CharField(max_length=100, null=True)
    runtime = models.CharField(max_length=10, null=True)
    genre = models.TextField(null=True)
    director = models.TextField(null=True)
    writer = models.TextField(null=True)
    actors = models.TextField(null=True)
    plot = models.TextField(null=True)
    language = models.TextField(null=True)
    awards = models.TextField(null=True)
    poster = models.TextField(null=True)
    ratings = models.TextField(null=True)
    metascore = models.TextField(null=True)
    imdb_rating = models.CharField(max_length=10, null=True)
    imdb_votes = models.CharField(max_length=10, null=True)
    imdb_id = models.CharField(max_length=10, null=True)
    c_type = models.CharField(max_length=10, null=True)
    dvd = models.TextField(null=True)
    box_office = models.TextField(null=True)
    production = models.TextField(null=True)
    website = models.TextField(null=True)
    added_on = models.DateTimeField("date added", auto_now_add=True)
    watched_on = models.DateTimeField("date watched", null=True)
    
    def __str__(self):
        return self.title
