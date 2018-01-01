from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from fincomm.models import Account, Transaction
# Create your views here.

@login_required
def display_transaction_list(request):
    account = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(debtor=account)
    if(account):
        return render(request,
            'fincomm/transaction_list.html',
            {'transactions': transactions}
        )

    return HttpResponse(status=403) #todo error page if no account exists
