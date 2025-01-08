from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "dashboard.html")

def investment(request):
    return render(request, "investment.html")

def loan(request):
    return render(request, "loan.html")

def editprofile(request):
    return render(request, "editprofile.html")

def preferences(request):
    return render(request, "preferences.html")  # Added preferences view

def security(request):
    return render(request, "security.html")  # Added security view

