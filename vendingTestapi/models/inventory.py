from django.db import models

class Inventory(models.Model):

    quantity = models.IntegerField(default=5)
    price = models.IntegerField(default=2)