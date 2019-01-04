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
from category.models import Category
from .choices import *
from .models import Transaction
from .forms import TransactionCreateForm
import json


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


def generate_spline(request):
    '''
    this method generate data for spline graph

    from each transactions between start date and end date,
    category and operation we take from user,
    we take date (formated) and money, and put them to the data list

    then we dumps to json format the data.
    '''
    choices = [i[0] for i in OPERATIONS_CHOICES]
    context = {
        'option_list': choices,
        'categories_list': Category.objects.filter(user=request.user),
    }
    if request.method == 'POST':
        try:
            start = request.POST['start']
            end = request.POST['end']
            option = request.POST['option']
            category = request.POST['category']
            category = Category.objects.get(name=category, user=request.user)
            data = Transaction.objects.filter(user=request.user, category=category, operation_type=option, pub_date__range=(start, end))
            data_for_graph = [[i.pub_date.strftime('%Y-%m-%d'), float(i.money)] for i in data]
            print(data_for_graph)
            context['data'] = json.dumps(data_for_graph)
            context['operation'] = option
        except:
            messages.warning(request, 'You should select date!')
            return redirect('spline')

    return render(request, 'transactions/spline_graph.html', context)


def generate_pie(request):
    '''

    this method generate data for pie graph,

    we take start date and end date, and operation
    from post request and filter all transactions by this data

    then 

    we take all categories and iterate them
    during iteration we take each category 
    and sum of money of each transactions in this category,

    then we put this sum and category name in list of data,
    and dumps this data to json format 
    ------------------------------------------
    example:
    data = []
    categories = ['food', 'rest']
    money_for_foor_transactions = [100, 200]
    money_for_rest_transactions = [500, 100]

    food => sum = 100+200
    data.append({name: food, y: sum})

    rest => sum = 500 + 100
    data.append({name: rest, y: sum})
    -------------------------------------------

    '''
    choices = [i[0] for i in OPERATIONS_CHOICES]
    context = {
        'option_list': choices,
    }
    if request.method == 'POST':
        try:
            start = request.POST['start']
            end = request.POST['end']
            option = request.POST['option']
            data = Transaction.objects.filter(user=request.user, operation_type=option, pub_date__range=(start, end))
            categories = Category.objects.filter(user=request.user)
            data_for_graph = []
            for category in categories:
                data_for_graph.append({'name': category.name, 'y': sum([float(i.money) for i in data.filter(category=category)])})

            print(data_for_graph)
            context['data'] = json.dumps(data_for_graph)
            context['data_for_table'] = data_for_graph
            context['operation'] = option
            context['start'] = start
            context['end'] = end
        except:
            messages.warning(request, 'You should select date!')
            return redirect('pie')

    return render(request, 'transactions/pie_graph.html', context)
