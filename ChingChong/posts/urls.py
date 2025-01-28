from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('create', views.postCreate, name='create_post'),
    path('all', views.postAll, name="all_posts"),
    path('mine', views.postMine, name="my_posts"),
    path('edit/<int:id>', views.postEdit, name="edit_post")
]