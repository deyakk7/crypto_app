from django.contrib.auth import get_user_model
from django.db import models

from storage.models import Storage

User = get_user_model()


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_name = models.CharField(max_length=100, choices=Storage.TOKEN_NAME)
    token_amount = models.DecimalField(max_digits=30, decimal_places=7)

    def __str__(self):
        return f'{self.user.username} {self.token_name} - {self.token_amount}'
