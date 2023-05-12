from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    # list_display = ['get_medicine']
    inlines = [
        OrderItemInline,
    ]

    def get_medicine(self, obj):
        print(obj.order_items__set.all)
        # return obj.order_items_set.all()
    
    # def get_quantity(self, obj):
    #    return obj.order_items.quantity

    # def get_price(self, obj):
    #     return obj.order_items.get_item_price



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)  