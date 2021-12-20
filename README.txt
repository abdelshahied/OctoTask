Here is the guide to use the api
Just append the path in between '--' to  (http://127.0.0.1:8000/api)
for example if you need to get all the users type (http://127.0.0.1:8000/api/get-all-users/)
and if you want to search a certain user(id=1) type (http://127.0.0.1:8000/api/get-user/1)


        Create Account-->            '/create-account/'
        Create Loan-->               '/create-loan/'
        Create Loan Installment-->   '/create-loan-ins/'


        Get All Users -->              '/get-all-users/'
        Get All Accounts -->           '/get-all-accounts/'
        Get All Loans -->              '/get-all-loans/'
        Get All Loans Installments-->  '/get-all-loan-ins/'

        Get OR Update Certain User [search by user id] -->               '/get-user/userid/'
        Get OR Update Certain Account [search by user id]-->             '/get-account/userid/'
        Get OR Update Certain Loan [search by user id]-->                '/get-loan/userid/'
        Get OR Update Certain Loan Installment [search by Loan id]-->    '/get-loan-ins/LoanId/'

        Delete Account [search by userid]-->  'delete-account/userid'

----------------------------------------------------------------------------------------------------------------------
Here is the code to run in 'manage.py shell' to insert sone samples in the database



from Loans.models import User, Account, Loan, LoanInstallment
from datetime import datetime, date
user1 = User(name='Mohamed', email='mohamed@octo.com', phone='01141885369', DateOfBirth= datetime(1999, 6, 28), id = 1)
user1.save()
user2 = User(name='Amr', email='amr@octo.com', phone='01141885367', DateOfBirth= datetime(1998, 6, 28), id = 2)
user2.save()
acc1 = Account(user = user1, balance = 1547.5, id = 1)
acc1.save()
acc2 = Account(user = user2, balance = 524.78, id = 2)
acc2.save()
loan1 = Loan(user = user1, status = 'Not Paid', amount = 1000.0, id = 1)
loan1.save()
loanins11 = LoanInstallment(loan = loan1, status = 'Not Paid', amount = 500.0, DueDate = datetime(2022, 1, 30), DatePaid = datetime(2022, 1, 30) , id = 1)
loanins11.save()
loanins12 = LoanInstallment(loan = loan1, status = 'Not Paid', amount = 500.0, DueDate = datetime(2022, 3, 30), DatePaid = datetime(2022, 3, 30), id = 2)
loanins12.save()
loan2 = Loan(user = user2, status = 'Not Paid', amount = 700.0)
loan2.save()
loanins21 = LoanInstallment(loan = loans, status = 'Not Paid', amount = 350.0, DatePaid = datetime(2022, 1, 30), DueDate = datetime(2022, 1, 30), id = 3)
loanins21.save()
loanins22 = LoanInstallment(loan = loans, status = 'Not Paid', amount = 350.0, DatePaid = datetime(2022, 3, 30), DueDate = datetime(2022, 3, 30), id = 4)
loanins22.save()
