from django.db import models

# Create your models here.
class Statement(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    choices = (("income", "income"), ("expense", "expense"))
    category = models.CharField(max_length=100, choices=choices)