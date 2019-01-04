from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm
    queryset = Category.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):  # this func check that the user which want to delete the post should be author of this post
        category = self.get_object()

        if self.request.user == category.user:
            return True
        else:
            return False

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)


class CategoryListView(LoginRequiredMixin, ListView):
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


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)

        except ProtectedError:
            messages.warning(request, f'You cannot delete this category')
            return redirect('home')

    def test_func(self):  # this func check that the user which want to delete the post should be author of this post
        category = self.get_object()

        if self.request.user == category.user:
            return True
        else:
            return False
