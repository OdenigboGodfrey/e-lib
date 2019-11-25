from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='staff-register'),
    path('login/', views.login, name='staff-login'),
]