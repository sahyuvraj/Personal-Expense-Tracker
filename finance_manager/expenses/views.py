from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
import csv
from django.http import HttpResponse

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/index.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def update_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/update_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return redirect('index')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Category', 'Amount', 'Description'])

    expenses = Expense.objects.all()
    for expense in expenses:
        writer.writerow([expense.date, expense.category, expense.amount, expense.description])

    return response
