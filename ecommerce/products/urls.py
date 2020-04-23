from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>', views.product_details, name='product_details'),
    path('featured/', views.featured_product_list, name='feaured_product_list'),
    path('featured/<int:pk>', views.featured_product_details, name='featured_product_details'),
]
