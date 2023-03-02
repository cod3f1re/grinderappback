# accounts/models.py
from django.contrib.auth.models import AbstractUser, models


class CustomUser(AbstractUser):
    pass

    # add additional fields in here
    date_of_birth = models.DateField(null=True, default='2023-08-23', blank=True)
    num_purchases = models.IntegerField(default=0)
    direction = models.CharField(max_length=200, default='', blank=True)
    rfc = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.username
