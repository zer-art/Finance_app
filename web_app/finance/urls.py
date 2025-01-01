from django.contrib import admin
from django.urls import path
from finance import views

urlpatterns = [
    path("", views.home, name="home"),
    path("investment/", views.investment, name="investment"),
]
