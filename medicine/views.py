from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView
)
from django.urls import reverse

from .models import Medicine


class ListMedicine(ListView):
    model = Medicine
    template_name = "medicine/medicine_list.html"


# class AddMedicine(CreateView):
#     model = Medicine
#     fields = '__all__'
#     success_url = reverse('medicine_list')


class UpdateMedicine(CreateView):
    pass


class DeleteMedicine(CreateView):
    pass