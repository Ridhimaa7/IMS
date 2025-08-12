# stock/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(
        "", 
        views.product_list, 
        name="product-list"                # matches redirect('product-list')
    ),
    path(
        "create/", 
        views.product_create, 
        name="product-create"
    ),
    path(
        "<int:pk>/edit/", 
        views.product_update, 
        name="product-edit"
    ),
    path(
        "<int:pk>/delete/", 
        views.product_delete, 
        name="product-delete"
    ),
    path('dashboard/', views.inventory_dashboard, name='inventory-dashboard'),

]
