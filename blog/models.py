import datetime
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.title} ==> {self.description} ... {self.date}'

