from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListOrder.as_view(), name='order_list'),
    path('<int:pk>/', views.DetailOrder.as_view(), name='order_detail'),
    path('create/', views.CreateOrder.as_view(), name='order_create'), 
    path('delete/<int:pk>/', views.DeleteOrder.as_view(), name='order_delete'),  
]