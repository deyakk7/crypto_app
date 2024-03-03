from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_transaction, name='create-transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete-transaction'),
    path('my/', views.TransactionListView.as_view(), name='my-transactions'),
    path('admin/all/', views.TransactionAdminListView.as_view(), name='admin-transactions'),
    path('admin/unwatched/', views.TransactionAdminUnWatchedListView.as_view(), name='admin-unwatched-transactions'),
    path('admin/accept/<int:pk>/', views.accept_transaction, name='accept-transaction'),
    path('admin/reject/<int:pk>/', views.reject_transaction, name='reject-transaction'),
]
