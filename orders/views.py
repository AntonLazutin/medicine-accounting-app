from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView, View
)
from django.urls import reverse_lazy

from .models import Order


class ListOrder(ListView):
    model = Order
    template_name = "orders/order_list.html"


class DetailOrder(DetailView):
    model = Order


# class UpdateOrder(UpdateView):
#     model = Order
#     exclude = ('id', 'date')


class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy("order_list")