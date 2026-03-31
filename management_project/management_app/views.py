from django.shortcuts import render, redirect
# from .form import userDataForm, bookDataForm, issueDataForm
# from .models import userData, bookData, issueData

def dashboard(request):
    return render(request, 'Dashboard.html')

    

def book_table(request):
    return render(request, 'BookTable.html')

def book_add(request):
    return render(request, 'BookAdd.html')

def book_details(request, book_id):
    return render(request, 'BookDetails.html')

def book_edit(request, book_id):
    return render(request, 'BookEdit.html')

def book_delete(request, book_id):
    return render(request, 'BookTable.html')



def user_table(request):
    return render(request, 'UserTable.html')

def user_add(request):
    return render(request, 'UserAdd.html')

def user_details(request, user_id):
    return render(request, 'UserDetails.html')

def user_edit(request, user_id):
    return render(request, 'UserEdit.html')

def user_delete(request, user_id):
    return render(request, 'UserTable.html')


def records_open(request):
    return render(request, 'RecordsOpen.html')


def records_closed(request):
    return render(request, 'RecordsClosed.html')


def records_borrow(request):
    return render(request, 'RecordsBorrowBook.html')
