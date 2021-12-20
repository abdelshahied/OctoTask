from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name="api-overview"),
    path('sign-up/', views.SignUp, name="SignUp"),

    path('get-all-users/', views.GetAllUsers, name="GetAllUsers"),
    path('get-all-accounts/', views.GetAllAccounts, name="GetAllAccounts"),
    path('get-all-loans/', views.GetAllLoans, name="GetAllLoans"),
    path('get-all-loan-ins/', views.GetAllLoanIns, name="GetAllLoanIns"),

    path('get-user/<str:pk>/', views.GetUser, name="GetUser"),
    path('get-account/<str:pk>/', views.GetAccount, name="GetAccount"),
    path('get-loan/<str:pk>/', views.GetLoan, name="GetLoan"),
    path('get-loan-ins/<str:pk>/', views.GetLoanIns, name="GetLoanIns"),

    path('delete-account/<str:pk>/', views.DeleteAccount, name="DeleteAccount"),
    path('create-account/', views.CreateAccount, name="CreateAccount"),
    path('create-loan/', views.CreateLoan, name="CreateLoan"),
    path('create-loan-ins/', views.CreateLoanIns, name="CreateLoanIns"),

]
