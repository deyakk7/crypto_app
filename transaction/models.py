from django.db import models

from storage.models import Storage
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token_name = models.CharField(max_length=100, choices=Storage.TOKEN_NAME)
    token_amount = models.FloatField()
    accepted = models.BooleanField(default=None, null=True)

    def __str__(self):
        return f"{self.user.username} {self.token_name}, {self.token_amount} - {self.accepted}"
