from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListOrder.as_view(), name='order_list'),
    path('<int:pk>/', views.DetailOrder.as_view(), name='order_detail'),  
]