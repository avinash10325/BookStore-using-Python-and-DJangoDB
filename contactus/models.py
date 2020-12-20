from django.db import models

# Create your models here.
class Messages(models.Model):
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    subject = models.CharField(max_length=100)