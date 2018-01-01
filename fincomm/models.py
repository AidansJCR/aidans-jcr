from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.get_full_name()

class Transaction(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    money_to_pay = models.DecimalField(max_digits=4, decimal_places=2)
    debtor = models.ForeignKey(Account, unique=False, related_name="debtor")
    def save(self, *args, **kwargs):
        # Set the created at date on first creation.
        if not self.id:
            self.created_at = timezone.now()
        super(Transaction, self).save(*args, **kwargs)
