from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Cities
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
def validate_birth_date(value):
    if value < date(1900, 1, 1):
        raise ValidationError("Дата рождения не может быть раньше 1900 года.")
    if value > date.today():
        raise ValidationError("Дата рождения не может быть в будущем.")
    
class User(AbstractUser):
    email = models.CharField("Email", max_length=50, blank=True, default='default@default.com')
    GENDERTYPE = [ ("M", "Мужской"), ("F","Женский"), ("D", "...") ]
    gender = models.CharField("Sex", max_length=10, choices=GENDERTYPE, default='D')
    number = models.CharField("Phone Number", default='', max_length=11, blank=True)
    birthday = models.DateField("Birthday Date", null=True, blank=True, validators=[validate_birth_date],)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
    food = models.CharField("Favorite Food", max_length=50, blank=True)
    aboutMe = models.TextField("About Me", max_length=256, blank=True, null=True)
