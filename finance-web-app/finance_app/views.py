from django.shortcuts import render
from django.http import JsonResponse
from .models import FinanceRecord

def index(request):
    return render(request, 'finance_app/index.html')

def get_finance_records(request):
    records = FinanceRecord.objects.all().values()
    return JsonResponse(list(records), safe=False)