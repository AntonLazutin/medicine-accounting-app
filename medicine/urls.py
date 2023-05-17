from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListMedicine.as_view(), name='medicine_list'),
    path('add/', views.CreateMedicine.as_view(), name='medicine_create'),
    path('<int:pk>/', views.DetailMedicine.as_view(), name='medicine_detail'),
    path('<int:pk>/delete/', views.DeleteMedicine.as_view(), name='medicine_delete'),
    path('<int:pk>/update/', views.UpdateMedicine.as_view(), name='medicine_update'), 
]