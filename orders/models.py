from django.db import models


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'order {self.date}'
    
    def get_total(self):
        total = 0
        for item in self.order_items.all():
            total += item.get_item_price()
        return total


class OrderItem(models.Model):
    medicine = models.ForeignKey('medicine.Medicine', related_name='order_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, 
                              related_name='order_items', 
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True)

    def get_item_price(self):
        return self.medicine.price * self.quantity
    
    def __str__(self) -> str:
        return f'{self.medicine.name} in order'
    