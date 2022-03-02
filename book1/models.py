from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
print( "in models.py")
class Book(models.Model):
    """class book information """
    name = models.CharField(max_length= 100)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = 1)

    class meta:
        db_table = "book"

    def __str__(self) :
        """string representation of book object"""
        return f"{self.name}"