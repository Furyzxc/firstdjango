from django.db import models


CATEGORIES = (
    ('default', 'default'),
    ('horror', 'horror'),
    ('comedy', 'comedy'),
    ('scifi', 'scifi')
)
# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    sinopsis = models.TextField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORIES, default='default')

    def __str__(self):
        return self.title