from django.shortcuts import render
from django.http import HttpResponse
from walletApp.models import Statement
from django.db.models import Sum # import aggregation function sum

# Create your views here.
def index(request):
    totalIncome = Statement.objects.filter(category="income").aggregate(Sum("amount"))
    totalExpense = Statement.objects.filter(category="expense").aggregate(Sum("amount"))
    #print(totalIncome)
    #print(totalExpense)
    return render(request, "index.html",{"income": totalIncome, "expense": totalExpense})

def account(request):
    data = Statement.objects.all()
    return render(request, "account.html", {"data": data})