from django.db import models

USER_CHOICES = (
    ('COMUM', 'Comum'),
    ('LOJISTA', 'Lojista'),
)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50, choices=USER_CHOICES, default='COMUM')
    name = models.CharField(max_length=200)
    registration = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    email = models.CharField(max_length=200, unique= True)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    