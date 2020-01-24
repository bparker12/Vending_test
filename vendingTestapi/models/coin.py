from django.db import models

class Coin(models.Model):

    quantity  = models.IntegerField(default=0)