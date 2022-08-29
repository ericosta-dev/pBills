from django.db import models

# Create your models here.


class Base(models.Model):
    """ Base Model """
    active = models.BooleanField(default=True)
    actualization = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Bank(Base):
    """ Bank Model """
    name = models.CharField(max_length=255, verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class Account(Base):
    """ Account Model """
    number = models.CharField(max_length=255, verbose_name='Number')
    agency = models.CharField(max_length=255, verbose_name='Agency')
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE, related_name='banks',blank=False)

    def __str__(self):
        return f'{self.bank} -> {self.number} : {self.agency}'


class Category(Base):
    """ Category Model """
    name = models.CharField(max_length=100, verbose_name='Category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Transaction(Base):
    """ Transaction Model """
    INFLOW = 'IN'
    OUTFLOW = 'OUT'

    TYPES = (
        (INFLOW, ('Inflow')),
        (OUTFLOW, ('Outflow')),
    )

    title = models.CharField(max_length=255, verbose_name='Title')
    type_payment = models.CharField(
        max_length=3, choices=TYPES, verbose_name='Type Payment')
    amount = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='Amount')
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='accounts')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.type_payment} : {self.title}'
