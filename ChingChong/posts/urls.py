from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('create', views.postCreate, name='create_post'),
    path('all', views.postCreate, name="all_posts"),
]