from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=30,unique=True)
    price = models.FloatField()
    #supplier
    description = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, related_name='medicines', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def in_stock(self):
        return self.amount > 0
    
    def purchased(self):
        if self.in_stock():
            self.amount -= 1