from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UsersCreateListView.as_view(), name='users-create-list'),
    path('users/<int:pk>/', views.UsersRetrieveUpdateDestroyView.as_view(), name='users-detail-view'),
]