from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    date_created = models.DateField()
    date_modified = models.DateField()
    date_inactive = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return "%s %s" % (self.title, self.price)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
