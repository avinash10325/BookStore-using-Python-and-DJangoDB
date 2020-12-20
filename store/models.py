from django.db import models

# Create your models here.
class Books(models.Model):
    Book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField(default=5)