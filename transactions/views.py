from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from transactions.models import Transactions
from transactions.serializers import TransactionsSerializer
from users.models import Users
from decimal import Decimal

class TransactionsCreateListView(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


    def perform_create(self, serializer):
       
        # Recupera os dados da requisição
        payer_id = self.request.data.get('payer')
        payee_id = self.request.data.get('payee')
        value = Decimal(self.request.data.get('value', 0.0))

        # Recupera os objetos de usuário com base nos IDs fornecidos
        payer = Users.objects.get(pk=payer_id)
        payee = Users.objects.get(pk=payee_id)
        
        if payer.balance <= 0:
            raise ValidationError("Usuário sem saldo.")

        if payer.user_type != 'COMUM':
            raise ValidationError("Lojistas não enviam dinheiro para ninguém. Transação recusada.")
        
        if value > payer.balance:
            raise ValidationError("Saldo insuficiente.")
        
        # Cria uma instância de Transaction
        transaction = Transactions.objects.create(payer=payer, payee=payee, value=value)
        
        # Atualiza o saldo dos usuários
        payer.balance = payer.balance - value
        payee.balance = payee.balance + value
        
        payer.save()
        payee.save()
        
        # Atualiza o serializer com a instância criada
        serializer.instance = transaction
    
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"ERROR": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        return response


class TransactionsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
