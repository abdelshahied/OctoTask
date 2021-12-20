import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, AccountSerializer, LoanSerializer, LoanInsSerializer
from .models import User, Account, Loan, LoanInstallment
import numpy as np
from datetime import datetime

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create User': '/sign-up/',
        'Create Account': '/create-account/',
        'Create Loan': '/create-loan/',
        'Create Loan Installment': '/create-loan-ins/',


        'Get All Users': '/get-all-users/',
        'Get All Accounts': '/get-all-accounts/',
        'Get All Loans': '/get-all-loans/',
        'Get All Loans Installments': 'get-all-loan-ins/',

        'Get OR Update Certain User [search by user id]': '/get-user/userid/',
        'Get OR Update Certain Account [search by user id]': '/get-account/userid/',
        'Get OR Update Certain Loan [search by user id]': '/get-loan/userid/',
        'Get OR Update Certain Loan Installment [search by Loan id]': '/get-loan-ins/LoanId/',

        'Delete Account [search by userid]': 'delete-account/userid',

    }
    return Response(api_urls)


@api_view(['POST', 'GET'])
def SignUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def GetAllUsers(request):
    try:
        users = User.objects.all()
    except:
        return Response('Not Found')

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def GetUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = UserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Updated")
        else:
            return Response("Failed")
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST', 'GET'])
def CreateAccount(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def GetAllAccounts(request):
    try:
        acc = Account.objects.all()
    except:
        return Response('Not Found')

    serializer = AccountSerializer(acc, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def DeleteAccount(request, pk):
    if request.method == 'GET':
        try:
            acc = Account.objects.get(pk=pk)
        except:
            return Response('Not Found')
        serializer = AccountSerializer(acc)
        return Response(serializer.data)
    if request.method == 'DELETE':
        try:
            acc = Account.objects.get(pk=pk).delete()
        except:
            return Response('Not Found')
        return Response('DELETED!!')

#by the user ID not by the Account ID
@api_view(['GET', 'PUT'])
def GetAccount(request, pk):
    try:
        user1 = User.objects.get(pk=pk)
        acc = Account.objects.filter(user=user1)
    except:
        return Response('Not Found')

    if request.method == 'PUT':
        serializer = AccountSerializer(acc, request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Updated")
        else:
            return Response("Failed")
    if request.method == 'GET':
        serializer = AccountSerializer(acc, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def CreateLoan(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def GetAllLoans(request):
    try:
        loans = Loan.objects.all()
    except:
        return Response('Not Found')
    try:
        serializer = LoanSerializer(loans, many=True)
    except:
        return Response('Error')

    return Response(serializer.data)

#search by the user ID
@api_view(['GET', 'PUT'])
def GetLoan(request, pk):
    try:
        user1 = User.objects.get(pk=pk)
        loan = Loan.objects.filter(user=user1)
    except:
        return Response('Not Found')

    if request.method=='GET':
        serializer = LoanSerializer(loan, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        if request.method == 'PUT':
            serializer = LoanSerializer(loan, request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated")
            else:
                return Response("Failed")


@api_view(['POST', 'GET'])
def CreateLoanIns(request):
    serializer = LoanInsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def GetAllLoanIns(request):
    try:
        loansins = LoanInstallment.objects.all()
    except:
        return Response('Not Found')
    serializer = LoanInsSerializer(loansins, many=True)
    return Response(serializer.data)


#search by Loan ID
@api_view(['GET', 'PUT'])
def GetLoanIns(request, pk):
    try:
        ln = Loan.objects.get(pk=pk)
        loanins = LoanInstallment.objects.filter(loan=ln)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = LoanInsSerializer(loanins, request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response("Updated")
        else:
            return Response("Failed")
    if request.method == 'GET':
        serializer = LoanInsSerializer(loanins, many=True)
        return Response(serializer.data)


# User Functions

# Read all his accounts (GetAccount/ search by the user)
# create new Account (CreateAccount)
# update current account (GetAccount)
# delete account (DeleteAccount)
# issue loan (CreateLoan + CreateLoanIns)
# view Loan (GetLoan) / (GetLoanIns)
# pay loan installments (GetLoanIns)
