from django.db import models

# Create your models here.
order_confirmation = ((1,"YES"),(0,"NO"))
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    email = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    confirmation = models.CharField(
        max_length = 10,
        choices = order_confirmation,
        default = 0
        )