from django.db import models


# https://qiita.com/ryubb_SU/items/06a5abd37515b9abf0fe
# class SampleData(models.Model):
#     lastName = models.CharField(max_length=128, verbose_name='Last name')
#     firstName = models.CharField(max_length=128, verbose_name='First name')
#     postalCode = models.CharField(max_length=128, verbose_name='Postal code')
#     telNumber = models.CharField(max_length=128, verbose_name='Tel number')
    
#     def __str__(self):
#         return f'{self.lastName} {self.firstName}

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name