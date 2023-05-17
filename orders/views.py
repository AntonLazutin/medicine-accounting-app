from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView, View
)
from django.urls import reverse_lazy

from .models import Order
from .forms import OrderForm, OrderItemFormSet
from django.db import transaction

class ListOrder(ListView):
    model = Order
    template_name = "orders/order_list.html"


class CreateOrder(CreateView):

    #TODO: ЗАПРЕТИТЬ ОДИНАКОВЫЕ ЛЕКАРСТВА В ЗАКАЗЕ

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order_list")
    template_name = 'orders/order_create.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OrderItemFormSet(self.request.POST)
        else: 
            context['formset'] = OrderItemFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.updated_by = self.request.user
            self.object = form.save()
        if form.is_valid() and formset.is_valid():
            formset.instance = self.object
            formset.save()
            self.object.update_amount()

        return super(CreateOrder, self).form_valid(form)
        
class DetailOrder(DetailView):
    model = Order


# class UpdateOrder(UpdateView):
#     model = Order
#     exclude = ('id', 'date')


class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy("order_list")