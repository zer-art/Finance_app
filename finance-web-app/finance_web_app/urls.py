from django.urls import path
from finance_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('finance/', views.finance_overview, name='finance_overview'),
    # Add more URL patterns as needed
]