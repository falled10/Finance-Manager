from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import (
    TransactionCreateView,
    TransactionListView,
    TransactionDeleteView,
    TransactionUpdateView,
)

urlpatterns = [
    path('transaction_create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('all_transactions/', TransactionListView.as_view(), name='all-transactions'),
    path('transaction/<int:pk>/delete', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transaction/<int:pk>/update', TransactionUpdateView.as_view(), name='transaction-update'),
    path('spline/', views.generate_spline, name='spline'),
    path('pie/', views.generate_pie, name='pie'),
]
