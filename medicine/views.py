from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView
)
from django.urls import reverse_lazy

from .models import Medicine
from .forms import MedicineForm


class ListMedicine(ListView):
    model = Medicine
    template_name = "medicine/medicine_list.html"


class DetailMedicine(DetailView):
    model = Medicine
    template_name = "medicine/medicine_detail.html"


class CreateMedicine(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_create.html'
    success_url = reverse_lazy('medicine_list')


class UpdateMedicine(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_update.html'
    success_url = reverse_lazy('medicine_list')


class DeleteMedicine(DeleteView):
    model = Medicine
    success_url = reverse_lazy('medicine_list')