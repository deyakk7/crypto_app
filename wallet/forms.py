from django.forms import ModelForm, NumberInput, ChoiceField

from wallet.models import Wallet


class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['token_name', 'token_amount']
        widgets = {
            'token_amount': NumberInput(attrs={'step': 0.01}),
        }
