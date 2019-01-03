from django import forms
from django.forms import ModelForm
from .models import Category, Transaction
from django.contrib.admin.widgets import AdminDateWidget
from .choices import *


# this form we use for show normal calendar in template
class DateInput(forms.DateInput):
    input_type = 'date'


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'brief_desctiption']


class TransactionCreateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    operation_type = forms.ChoiceField(choices=OPERATIONS_CHOICES, required=True)
    pub_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Transaction
        fields = ['category', 'operation_type', 'money', 'brief_desctiption', 'pub_date']
