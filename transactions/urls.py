from django.urls import path
from . import views


urlpatterns = [
    path('transactions/', views.TransactionsCreateListView.as_view(), name='transactions-create-list'),
    path('transactions/<int:pk>/', views.TransactionsRetrieveUpdateDestroyView.as_view(), name='transactions-detail-view'),
]