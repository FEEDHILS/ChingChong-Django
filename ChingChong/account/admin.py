from django.contrib import admin
from . models import *
from django.templatetags.static import static
from django.contrib.auth.admin import UserAdmin

# Пока хотя бы так
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'gender', 'date_joined', 'is_active', 'is_staff')
    fieldsets = list(UserAdmin.fieldsets)
    # Видоизменяем стандартные fieldsets
    fieldsets[0] = (
        None,
        {
            'fields': ('username', 'password', 'email'),  # Перемещаем email сюда
        },
    )
    fieldsets[1] = (
        'Personal Info',
        {
            'fields': ('gender', 'number', 'city', 'food', 'birthday',),  # Перевернули тут все вверх-дном!!
        },
    )