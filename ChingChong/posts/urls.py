from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.postCreate, name='create_post'),
]