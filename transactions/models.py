from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    brief_description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category-create')


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    operation_type = models.CharField(max_length=200)
    money = models.DecimalField(decimal_places=2, max_digits=10000)
    brief_description = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return f'{self.brief_description}'

    def get_absolute_url(self):
        return reverse('transaction-create')
