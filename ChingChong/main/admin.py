from django.contrib import admin
from .models import *

# Здесь могла бы быть ваша реклама
# admin.site.register(Cities)
@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city', 'adress',)
    