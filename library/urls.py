from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('items/add/', views.add, name='library-add-item'),
    path('items/', views.items, name='library-get-items'),
    path('items/borrow/<int:item_id>/', views.borrow, name='library-borrow-item'),
    path('items/borrowed/<int:user_id>/', views.borrowed, name='library-get-borrowed-items'),
]