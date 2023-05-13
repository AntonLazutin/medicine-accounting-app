from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=40)
    house = models.IntegerField()

    class Meta:
        verbose_name_plural = 'adresses'

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'


class Pharmacy(models.Model):
    address = models.ForeignKey(Address, related_name='pharmacies', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'pharmacies'

    def __str__(self):
        return f'Аптека по адресу {self.address}' 