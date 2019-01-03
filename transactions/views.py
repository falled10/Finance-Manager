from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
)
from .models import Category, Transaction
from .forms import CategoryCreateForm, TransactionCreateForm


class CategoryCreateView(CreateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm


class TransactionCreateView(CreateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm


class CategoryListView(ListView):
    template_name = 'transactions/all_categories.html'
    queryset = Category.objects.all()


class TransactionListView(ListView):
    template_name = 'transactions/all_transactions.html'
    queryset = Transaction.objects.all()
