from argparse import Action
from unicodedata import category
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Bank, Account, Category, Transaction
from .serializers import (BankSerializer,
                        CategorySerializer,
                        AccountSerializer,
                        TransactionSerializer)

# pylint: disable=E1101
class BankAPIView(viewsets.ModelViewSet):
    """Bank API View"""
    queryset = Bank.objects.filter(active=True)
    serializer_class = BankSerializer


class AccountAPIView(viewsets.ModelViewSet):
    """Account API View"""
    queryset = Account.objects.filter(active=True)
    serializer_class = AccountSerializer

    @action(detail=True,methods=['get'])
    def transactions(self,request, pk=None):
        account = self.get_object()
        transaction = Transaction.objects.filter(account=account,active=True)
        serializer = TransactionSerializer(transaction,many=True)
        return Response(serializer.data)


class CategoryAPIView(viewsets.ModelViewSet):
    """Category API View"""
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer


class TransactionAPIView(viewsets.ModelViewSet):
    """Transaction API View"""
    queryset = Transaction.objects.filter(active=True)
    serializer_class = TransactionSerializer
