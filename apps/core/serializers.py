from django.db.models import Avg,Sum
from rest_framework import serializers

from .models import Transaction, Bank, Account, Category

# pylint: disable=C0115
# pylint: disable=E1101
class BankSerializer(serializers.ModelSerializer):
    """ Bank Serializer """

    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'active',
            'actualization',
            'created',
        )


class AccountSerializer(serializers.ModelSerializer):
    """ Account Serializer"""

    amount_inflow = serializers.SerializerMethodField()
    def get_amount_inflow(self,obj):
        """Get amount inflow transactions"""
        account = obj
        in_transactions = Transaction.objects.filter(account=account,
                                                        type_payment='IN',
                                                        active=True).aggregate(Sum('amount'))
        in_transactions =  in_transactions['amount__sum']
        return in_transactions


    amount_outflow = serializers.SerializerMethodField()
    def get_amount_outflow(self,obj):
        """Get amount outflow transactions"""
        account = obj
        out_transactions = Transaction.objects.filter(account=account,type_payment='OUT',active=True).aggregate(Sum('amount'))
        out_transactions = out_transactions['amount__sum']
        return out_transactions


    actual_balance = serializers.SerializerMethodField()
    def get_actual_balance(self,obj):
        """Get actual balance"""
        account = obj
        amount_in = Transaction.objects.filter(account=account,
                                                type_payment='IN',
                                                active=True).aggregate(Sum('amount'))
        amount_out = Transaction.objects.filter(account = account,
                                                type_payment='OUT',
                                                active=True).aggregate(Sum('amount'))

        amount_in = amount_in['amount__sum']
        amount_out = amount_out['amount__sum']

        return amount_in - amount_out

    class Meta:
        model = Account
        fields = (
            'id',
            'number',
            'agency',
            'bank',
            'active',
            'actualization',
            'created',
            'amount_inflow',
            'amount_outflow',
            'actual_balance',
        )


class CategorySerializer(serializers.ModelSerializer):
    """ Category Serializer """

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'active',
            'actualization',
            'created',
        )


class TransactionSerializer(serializers.ModelSerializer):
    """ Transaction Serializer """

    class Meta:
        model = Transaction
        fields = (
            'id',
            'title',
            'type_payment',
            'amount',
            'account',
            'category',
            'active',
            'actualization',
            'created',
        )
# pylint: enable=C0115
# pylint: enable=E1101
