from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    DateOfBirth = models.DateTimeField()
    
    def __str__(self):
        return self.name


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    DateCreated = models.DateTimeField(default=timezone.now())


class Loan(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    amount = models.FloatField()
    DateCreated = models.DateTimeField(default=timezone.now())


class LoanInstallment(models.Model):
    id = models.IntegerField(primary_key=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    amount = models.FloatField()
    DatePaid = models.DateTimeField()
    DueDate = models.DateTimeField()
