from rest_framework.routers import SimpleRouter

from .views import (BankAPIView,
                    AccountAPIView,
                    CategoryAPIView,
                    TransactionAPIView)

router = SimpleRouter()
router.register('banks',BankAPIView)
router.register('accounts',AccountAPIView)
router.register('categories',CategoryAPIView)
router.register('transactions',TransactionAPIView)
