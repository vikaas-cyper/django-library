from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('category/', views.CategoryController.index, name='category_list'),
    path('category/create/', views.CategoryController.create, name='category_create'),
    path('category/<int:pk>/', views.CategoryController.view, name='category_detail'),
    path('category/<int:pk>/delete', views.CategoryController.delete, name='category_delete'),
    
]
