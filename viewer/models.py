import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class ShowSector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    show = models.ManyToManyField(ShowSector, blank=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.CharField(max_length=10)
    ulje_perqindje = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    sales = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    images = models.ImageField(default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.price)
