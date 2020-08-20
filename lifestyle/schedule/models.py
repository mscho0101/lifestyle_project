from django.db import models


# Create your models here.


class Schedule(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    location = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    theme = models.CharField(max_length=200)
    memo = models.TextField(blank=True)