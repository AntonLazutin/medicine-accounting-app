from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=30,unique=True)
    price = models.FloatField()
    #supplier
    description = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    def in_stock(self):
        return self.amount > 0
    
    def purchased(self):
        if self.in_stock():
            self.amount -= 1