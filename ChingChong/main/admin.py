from django.contrib import admin
from .models import User

# Пока хотя бы так
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass