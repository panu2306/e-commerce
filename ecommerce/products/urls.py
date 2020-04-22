from django.urls import path, include

from . import views

urlpatterns = [
    path('index/', views.product_list, name='product_list'),
    path('<int:pk>', views.product_details, name='product_details'),
]
