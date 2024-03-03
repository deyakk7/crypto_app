import decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction as trans

from storage.mixins import SuperUserRequiredMixin
from wallet.forms import WalletForm
from wallet.models import Wallet
from wallet.utils import get_token_prices

User = get_user_model()


class WalletListView(LoginRequiredMixin, ListView):
    model = Wallet
    template_name = 'wallet/wallet-list.html'
    context_object_name = 'wallets'

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


@login_required
def wallet_converter(request, pk):
    current_wallet = Wallet.objects.get(pk=pk)
    form = WalletForm()
    context = {
        'current_wallet': current_wallet,
        'form': form
    }

    if request.method == 'POST':
        form = WalletForm(request.POST)
        wallet = form.save(commit=False)
        if wallet.token_amount > current_wallet.token_amount:
            context['error'] = 'Not enough tokens'
            context['form'] = form
            return render(request, 'wallet/wallet-converter.html', context)

        if form.is_valid():
            data = get_token_prices()
            data['USDT'] = 1
            result_value = wallet.token_amount * decimal.Decimal(data[current_wallet.token_name])

            if wallet.token_name != "USDT":
                result_value /= decimal.Decimal(data[wallet.token_name])

            with trans.atomic():
                new_wallet = Wallet.objects.filter(user=request.user, token_name=wallet.token_name).first()
                if new_wallet:
                    new_wallet.token_amount += result_value
                    new_wallet.save()
                else:
                    Wallet.objects.create(
                        user=request.user,
                        token_name=wallet.token_name,
                        token_amount=result_value
                    )
                current_wallet.token_amount -= wallet.token_amount
                current_wallet.save()

            return redirect(reverse('my-wallets'))

    return render(request, 'wallet/wallet-converter.html', context)


class UserAdminListView(SuperUserRequiredMixin, ListView):
    model = User
    template_name = 'wallet/users-admin-list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class WalletAdminListView(SuperUserRequiredMixin, ListView):
    model = Wallet
    template_name = 'wallet/wallet-admin-list.html'
    context_object_name = 'wallets'

    def get_queryset(self):
        return Wallet.objects.all().filter(user_id=self.kwargs['pk'])
