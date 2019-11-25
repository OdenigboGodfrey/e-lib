from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='client-register'),
    path('login/', views.login, name='client-login'),
]