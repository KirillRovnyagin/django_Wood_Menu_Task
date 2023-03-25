from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(blank=True)