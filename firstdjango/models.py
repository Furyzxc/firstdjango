from django.db import models
from django.contrib.auth.models import User


CATEGORIES = (
    ('default', 'default'),
    ('horror', 'horror'),
    ('comedy', 'comedy'),
    ('scifi', 'scifi')
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORIES, default='default')

    def __str__(self):
        return self.title