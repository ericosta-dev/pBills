from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import Transaction, Bank, Account, Category

# pylint: disable=C0115
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
