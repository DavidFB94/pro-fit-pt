from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<composite_key>/', views.remove_from_cart, name='remove_from_cart'),
]
