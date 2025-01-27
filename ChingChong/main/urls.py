from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="main/index.html"), name="index"),
    path('menu', TemplateView.as_view(template_name="main/menu.html"), name="menu"),
    path('contacts', TemplateView.as_view(template_name="main/contacts.html"), name="contacts"),
    path('subs', TemplateView.as_view(), name="subscription"),
    path('api/search_city', views.search_city),
    path('api/profile_update', views.profile_update),
]