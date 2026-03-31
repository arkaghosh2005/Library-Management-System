from django.shortcuts import render, redirect
from .form import *
from .models import *


def dashboard(request):
    total_users = userData.objects.count()
    total_books = bookData.objects.count()
    borrowed_books = issueBookData.objects.filter(status='issued').count()
    returned_books = issueBookData.objects.filter(status='returned').count()
    #TODO: which table to use for "recent-table"

    return render(request, 'Dashboard.html',{
        'total_users': total_users,   
        'total_books': total_books, 'borrowed_books': borrowed_books, 'returned_books': returned_books
        })
    

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
    users = userData.objects.all()
    return render(request, 'UserTable.html', {'users': users})


def user_add(request):
    if request.method == 'POST':
        form=userDataForm(request.POST)
        if form.is_valid(): 
            form.save() # saves the data into the database
            # auto converts the data to required types
            return redirect("user_table")
        else: 
            return render(request, 'UserAdd.html', {"form":form})
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
