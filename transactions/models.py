from django.db import models
from users.models import Users

class Transactions(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    payer = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='sent_transactions')
    payee = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='received_transactions')

    def __str__(self):
        return f"{self.payer} to {self.payee} - {self.value}"