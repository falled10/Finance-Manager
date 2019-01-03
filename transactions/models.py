from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    brief_desctiption = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} category'


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    operation_type = models.CharField(max_length=200)
    money = models.DecimalField(decimal_places=2, max_digits=10000)
    brief_desctiption = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return f'{self.brief_desctiption}'
