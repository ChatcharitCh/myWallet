from django.shortcuts import render
from django.http import HttpResponse
from walletApp.models import Statement

# Create your views here.
def index(request):
    return render(request, "index.html")

def account(request):
    data = Statement.objects.all()
    return render(request, "account.html", {"data": data})