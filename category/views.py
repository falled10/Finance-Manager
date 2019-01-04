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
from .models import Category
from .forms import CategoryCreateForm
import json


class CategoryCreateView(CreateView):
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm
    queryset = Category.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryListView(ListView):
    template_name = 'category/all_categories.html'

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


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)

        except ProtectedError:
            messages.warning(request, f'You cannot delete this category')
            return redirect('home')
