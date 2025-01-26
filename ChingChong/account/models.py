from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Cities

# Create your models here.
class User(AbstractUser):
    email = models.CharField("Email", max_length=50, blank=True, default='default@default.com')
    GENDERTYPE = [ ("M", "Male"), ("F","Female"), ("D", "Undefined") ]
    gender = models.CharField("Sex", max_length=10, choices=GENDERTYPE, default='D')
    number = models.CharField("Phone Number", default='', max_length=11, blank=True)
    birthday = models.DateField("Birthday Date", null=True, blank=True)
    # city = models.CharField("City", max_length=256, blank=True)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
    food = models.CharField("Favorite Food", max_length=50, blank=True)
