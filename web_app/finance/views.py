from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "dashboard.html")

def investment(request):
    return render(request, "investment.html")