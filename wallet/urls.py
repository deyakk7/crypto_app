from django.urls import path

from . import views

urlpatterns = [
    path('my/', views.WalletListView.as_view(), name='my-wallets'),
    path('converter/<int:pk>/', views.wallet_converter, name='wallet-converter'),
    path('admin/', views.UserAdminListView.as_view(), name='admin-users'),
    path('admin/wallets/<int:pk>/', views.WalletAdminListView.as_view(), name='admin-wallets'),
]