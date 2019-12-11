from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.IntegerField(max_length=10)

    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())


class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())

