from django.urls import path
from . import views

urlpatterns = [
    path('items/add/', views.add, name='library-add-item'),
    path('items/', views.items, name='library-get-items'),
    path('items/borrow/<int:item_id>', views.borrow, name='library-borrow-item')
]