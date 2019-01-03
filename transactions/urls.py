from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import (
    CategoryCreateView,
    TransactionCreateView,
    CategoryListView,
    TransactionListView
)

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category-create'),
    path('transaction_create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('all_categories/', CategoryListView.as_view(), name='all-categories'),
    path('all_transactions/', TransactionListView.as_view(), name='all-transactions'),
]
