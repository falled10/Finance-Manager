from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import (
    CategoryCreateView,
    CategoryListView,
    CategoryDeleteView,
    CategoryUpdateView,
)

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category-create'),
    path('all_categories/', CategoryListView.as_view(), name='all-categories'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category-update'),
]
