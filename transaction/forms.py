from django import forms

from .models import Transaction, Storage
from django.contrib.auth.models import User


class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['token_name'].choices = [(storage.token_name, storage.token_name) for storage in
                                             Storage.objects.all()]

    class Meta:
        model = Transaction
        fields = ['token_name', 'token_amount']
