from django.db import models

# Create your models here.
class ShortUrl(models.Model):

    original_url = models.URLField(max_length=10000)
    short_url = models.CharField(max_length = 100)
    created_on = models.DateTimeField()
