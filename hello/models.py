from django.db import models

# Create your models here.
class Hello(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default="This is default summary")