from django.forms import ModelForm

from .models import Storage


class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ['token_name', 'value']


class StorageFormUpdate(ModelForm):
    class Meta:
        model = Storage
        fields = ['value']