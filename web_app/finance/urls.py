from django.contrib import admin
from django.urls import path
from finance import views

urlpatterns = [
    path("", views.home, name="home"),
    path("investment/", views.investment, name="investment"),
    path("loan/", views.loan, name="loan"),  # Added loan URL
    path("editprofile/", views.editprofile, name="editprofile"),  # Added 
    path("preferences/", views.preferences, name="preferences"),  # Added preferences URL
    path("security/", views.security, name="security"),  # Added security URL
]
