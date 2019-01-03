from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import (
    CategoryCreateView,
    TransactionCreateView,
    CategoryListView,
    TransactionListView,
    TransactionDeleteView,
    CategoryDeleteView,
    TransactionUpdateView,
    CategoryUpdateView,
)

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category-create'),
    path('transaction_create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('all_categories/', CategoryListView.as_view(), name='all-categories'),
    path('all_transactions/', TransactionListView.as_view(), name='all-transactions'),
    path('transaction/<int:pk>/delete', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    path('transaction/<int:pk>/update', TransactionUpdateView.as_view(), name='transaction-update'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category-update'),
]
