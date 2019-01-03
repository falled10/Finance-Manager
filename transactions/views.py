from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CategoryCreateForm, TransactionCreateForm


class CategoryCreateView(CreateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm


class TransactionCreateView(CreateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm
