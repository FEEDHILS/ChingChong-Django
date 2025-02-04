from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('password_reset', views.forgot, name='reset'),
    path('password_reset/confirmed', TemplateView.as_view(template_name="account/resetConfirm.html"), name='reset_confirmed'),
    path('password_reset/<uidb64>/<token>/', views.reset_confirmed, name='password_reset'),
    path('profile/<str:name>/', views.profile, name="check_profile"),
    path('profile/', views.profile, name="profile"),
]