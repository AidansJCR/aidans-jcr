from django.shortcuts import render


# Create your views here.
def finance_home(request):
    return render(request, 'finance_home.html')
