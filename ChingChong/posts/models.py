from django.db import models
from account.models import User
from main.models import Restaurant

# Create your models here.
class Post(models.Model):
    RATINGTYPE = [ (1, "1 Звезда"), (2,"2 Звезды"), (3, "3 Звезды"), (4, "4 Звезды"), (5, "5 Звезд") ]
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.IntegerField("Рейтинг", choices=RATINGTYPE, default='5', blank=False)
    review = models.TextField("Отзыв", blank=False, max_length=1024)

    publish = models.BooleanField("Опубликован", default=False)