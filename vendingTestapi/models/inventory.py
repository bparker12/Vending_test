from django.db import models

class Inventory(models.Model):

    name = models.CharField(max_length=50, default="")
    quantity = models.IntegerField(default=5)
    price = models.IntegerField(default=2)