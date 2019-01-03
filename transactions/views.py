from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from .models import Category, Transaction
from .forms import CategoryCreateForm, TransactionCreateForm


class CategoryCreateView(CreateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm


class TransactionCreateView(CreateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm


class TransactionUpdateView(UpdateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm
    queryset = Transaction.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm
    queryset = Category.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryListView(ListView):
    template_name = 'transactions/all_categories.html'
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        category = request.POST['category']
        object_list = Category.objects.filter(name__startswith=category)
        context = {
            'object_list': object_list,
        }
        return render(request, self.template_name, context)


class TransactionListView(ListView):
    template_name = 'transactions/all_transactions.html'
    queryset = Transaction.objects.all()

    def post(self, request, *args, **kwargs):
        transaction = request.POST['transaction']
        category = Category.objects.get(name=transaction)
        object_list = Transaction.objects.filter(category=category)
        context = {
            'object_list': object_list,
            'category_list': Category.objects.all()
        }
        return render(request, self.template_name, context)


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/delete_transaction.html'
    success_url = '/'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'transactions/delete_category.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)

        except ProtectedError:
            messages.warning(request, f'You cannot delete this category')
            return redirect('home')
