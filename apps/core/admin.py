from django.contrib import admin

# Register your models here.
from .models import Transaction,Bank,Account,Category

admin.site.register(Transaction)
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Category)
