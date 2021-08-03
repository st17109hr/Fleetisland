from django.db import models
from django.utils import timezone

# Create your models here.

class Fleet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    text = models.CharField(max_length=140, verbose_name='Fleet')
    date = models.TimeField(auto_now_add=True)
    def __str__(self):
        return str(self.date)