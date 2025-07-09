from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'accounts/home.html')

def create_account(request):
    if request.method == 'POST':
        name = request.POST['name']
        acc_no = request.POST['account_number']
        if Account.objects.filter(account_number=acc_no).exists():
            messages.error(request, "Account number already exists.")
        else:
            Account.objects.create(name=name, account_number=acc_no)
            messages.success(request, "Account created successfully.")
            return redirect('home')
    return render(request, 'accounts/create_account.html')

def access_account(request):
    if request.method == 'POST':
        acc_no = request.POST['account_number']
        try:
            account = Account.objects.get(account_number=acc_no)
            return render(request, 'accounts/dashboard.html', {'account': account})
        except Account.DoesNotExist:
            messages.error(request, "Account not found.")
    return render(request, 'accounts/access_account.html')

def deposit(request, acc_no):
    account = get_object_or_404(Account, account_number=acc_no)
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        account.balance += amount
        account.save()
        messages.success(request, f"Deposited KES {amount}")
        return redirect('access')
    return render(request, 'accounts/deposit.html', {'account': account})

def withdraw(request, acc_no):
    account = get_object_or_404(Account, account_number=acc_no)
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        if amount > account.balance:
            messages.error(request, "Insufficient balance.")
        else:
            account.balance -= amount
            account.save()
            messages.success(request, f"Withdrew KES {amount}")

            def user_dashboard(request, acc_no):
    account = get_object_or_404(Account, acc_no=acc_no)
    transactions = Transaction.objects.filter(account=account).order_by('-date')[:5]  # Latest 5
    context = {
        'account': account,
        'transactions': transactions,
    }
    return render(request, 'accounts/user_dashboard.html', context)


@staff_member_required
def admin_dashboard(request):
    accounts = Account.objects.all()
    transactions = Transaction.objects.all().order_by('-date')[:10]
    context = {
        'accounts': accounts,
        'transactions': transactions,
    }
    return render(request, 'accounts/admin_dashboard.html', context)

