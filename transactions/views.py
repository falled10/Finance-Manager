from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import ProtectedError
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from .models import Category, Transaction
from .forms import CategoryCreateForm, TransactionCreateForm
import json


class CategoryCreateView(CreateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class TransactionCreateView(CreateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class TransactionUpdateView(UpdateView):
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm
    queryset = Transaction.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    template_name = 'transactions/category_create.html'
    form_class = CategoryCreateForm
    queryset = Category.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryListView(ListView):
    template_name = 'transactions/all_categories.html'

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

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

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

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


def generate_spline(request):
    context = {
        'option_list': Transaction.objects.filter(user=request.user),
        'categories_list': Category.objects.filter(user=request.user),
    }
    if request.method == 'POST':
        try:
            start = request.POST['start']
            end = request.POST['end']
            option = request.POST['option']
            category = request.POST['category']
            category = Category.objects.get(name=category)
            data = Transaction.objects.filter(user=request.user, category=category, operation_type=option, pub_date__range=(start, end))
            data_for_graph = [[i.pub_date.strftime('%Y-%m-%d'), float(i.money)] for i in data]
            print(data_for_graph)
            context['data'] = json.dumps(data_for_graph)
        except:
            messages.warning(request, 'You should select date!')
            return redirect('spline')

    return render(request, 'transactions/spline_graph.html', context)


def generate_pie(request):
    context = {
        'option_list': Transaction.objects.filter(user=request.user),
        'categories_list': Category.objects.filter(user=request.user),
    }
    if request.method == 'POST':
        try:
            start = request.POST['start']
            end = request.POST['end']
            option = request.POST['option']
            data = Transaction.objects.filter(user=request.user, operation_type=option, pub_date__range=(start, end))
            categories = Category.objects.all()
            data_for_graph = []
            for category in categories:
                data_for_graph.append({'name': category.name, 'y': sum([float(i.money) for i in data.filter(category=category)])})

            print(data_for_graph)
            context['data'] = json.dumps(data_for_graph)
        except:
            messages.warning(request, 'You should select date!')
            return redirect('pie')

    return render(request, 'transactions/pie_graph.html', context)
