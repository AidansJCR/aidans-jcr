from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TransactionInfo(models.Model):
    """ The information about a given transaction, i.e. formal payment. Displays in the user's dashboard """
    name = models.CharField(max_length=256)
    description = models.TextField()

class Transaction(models.Model):
    """An individual transaction for a person. Prices are in £ sterling"""
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    payee = models.ForeignKey(User)
    transaction_info = models.ForeignKey(TransactionInfo)

    def __str__():
        """Display the transaction name as being the username and transaction name """
        return str(name) + payee.get_username()
