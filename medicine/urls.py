from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListMedicine.as_view(), name='medicine_list'),
    path('add/', views.CreateMedicine.as_view(), name='medicine_create'),
]