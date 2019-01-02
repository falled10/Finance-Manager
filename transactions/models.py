from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    brief_desctiption = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} category'
