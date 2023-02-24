from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


# Create your models here.
class User(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=50, null=False, blank=True)
    surname = models.CharField(max_length=50, null=False, blank=True)
    username = models.CharField(max_length=50, null=False, blank=True)
    purchasesCount = models.IntegerField()
    password = models.TextField(max_length=20, null=False)
    birthdate = models.DateTimeField(auto_now_add=True, verbose_name="birth date")
    date_creation = models.DateTimeField(auto_now=True, verbose_name="date register")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

