from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    RATINGTYPE = [ ("1", 1), ("2",2), ("3", 3), ("4", 4), ("5", 5) ]
    rating = models.IntegerField("Рейтинг", choices=RATINGTYPE, default='5', blank=True)
    review = models.TextField("Отзыв", blank=True)