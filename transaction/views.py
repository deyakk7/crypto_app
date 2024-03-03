from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction as trans
from django.shortcuts import render, redirect
from django.views.generic import ListView

from storage.mixins import SuperUserRequiredMixin
from storage.models import Storage
from wallet.models import Wallet
from .forms import TransactionForm
from .models import Transaction


@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.user = request.user
            new_transaction.save()
            return redirect('my-transactions')
    else:
        form = TransactionForm()
    return render(request, 'transaction/transaction-add.html', {'form': form})


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction-list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if transaction.accepted is None:
        transaction.delete()
    return redirect('my-transactions')


class TransactionAdminListView(SuperUserRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction/transaction-list-admin.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.all()


class TransactionAdminUnWatchedListView(SuperUserRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction/transaction-list-admin.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(accepted=None)


@login_required()
@permission_required('is_superuser')
def accept_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if transaction.accepted is not None:
        return redirect('admin-transactions')

    storage_token = Storage.objects.filter(token_name=transaction.token_name).first()
    if storage_token:
        with trans.atomic():
            if transaction.token_amount > storage_token.value:
                transaction.accepted = False
                transaction.save()
                return redirect('admin-transactions')

            storage_token.value -= transaction.token_amount
            storage_token.save()
            wallet = Wallet.objects.filter(user=transaction.user, token_name=transaction.token_name).first()
            if wallet:
                wallet.token_amount += transaction.token_amount
                wallet.save()
            else:
                Wallet.objects.create(
                    user=transaction.user,
                    token_name=transaction.token_name,
                    token_amount=transaction.token_amount
                )

            transaction.accepted = True
            transaction.save()
    return redirect('admin-transactions')


@login_required()
@permission_required('is_superuser')
def reject_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if transaction.accepted is not None:
        return redirect('admin-transactions')
    transaction.accepted = False
    transaction.save()
    return redirect('admin-transactions')