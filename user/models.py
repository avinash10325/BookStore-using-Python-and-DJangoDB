from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(blank=False, max_length=20)
    name = models.CharField(max_length=50, default='name')