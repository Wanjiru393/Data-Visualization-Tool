from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('product/', views.product, name='product'),
path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
path('product/edit/<int:pk>/', views.product_edit, name='product_edit'),
path('user/', views.user, name='user'),
path('order/', views.order, name='order'),



]