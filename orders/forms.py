from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        exclude = ('id',)

class OrderItemForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        exclude = ('id', 'order',)

OrderItemFormSet = forms.inlineformset_factory(Order, OrderItem, exclude=('id',), can_delete=False, extra=1)

