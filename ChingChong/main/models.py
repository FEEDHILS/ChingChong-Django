from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("Имя", max_length=50)
    login = models.CharField("Логин", max_length=30)
    password = models.TextField("Пароль", max_length=20)
