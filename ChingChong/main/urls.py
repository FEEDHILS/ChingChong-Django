from django.urls import path, include
from . import views
from .models import User
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('menu', TemplateView.as_view(template_name="menu.html"), name="menu"),
    path('contacts', TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path('subs', TemplateView.as_view(), name="subscription"),
    path('registration', TemplateView.as_view(), name="registration"),
    path('', include('django.contrib.auth.urls')),
]