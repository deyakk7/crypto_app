from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from storage.forms import StorageForm, StorageFormUpdate
from storage.mixins import SuperUserRequiredMixin
from storage.models import Storage


class StorageListView(SuperUserRequiredMixin, ListView):
    model = Storage
    template_name = 'storage/storage.html'
    context_object_name = 'storage'


class StorageCreateView(SuperUserRequiredMixin, CreateView):
    model = Storage
    form_class = StorageForm
    template_name = 'storage/storage_add.html'
    success_url = '/storage/'


class StorageUpdateView(SuperUserRequiredMixin, UpdateView):
    model = Storage
    form_class = StorageFormUpdate
    template_name = 'storage/storage_add.html'
    success_url = '/storage/'


@login_required
@permission_required('is_superuser')
def delete(request, pk):
    Storage.objects.filter(id=pk).delete()
    return redirect(reverse('storage-list'))
