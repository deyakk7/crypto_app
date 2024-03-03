from django.urls import path

from . import views

urlpatterns = [
    path('', views.StorageListView.as_view(), name='storage-list'),
    path('add/', views.StorageCreateView.as_view(), name='storage-add'),
    path('update/<int:pk>/', views.StorageUpdateView.as_view(), name='storage-update'),
    path('delete/<int:pk>/', views.delete, name='storage-delete'),
]
