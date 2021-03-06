from django import forms
from django.forms import ModelForm
from .models import Transaction
from category.models import Category
from django.contrib.admin.widgets import AdminDateWidget
from .choices import *


# this form we use for show normal calendar in template
class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionCreateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)

    # here we got choices from choices.py file and put them to select field in template
    operation_type = forms.ChoiceField(choices=OPERATIONS_CHOICES, required=True)
    pub_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Transaction
        fields = ['category', 'operation_type', 'money', 'brief_description', 'pub_date']

    def __init__(self, user=None, **kwargs):
        super(TransactionCreateForm, self).__init__(**kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)
