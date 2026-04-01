from django.shortcuts import render, redirect
from django.db.models import Q  
from .form import *
from .models import *
# Q allows building complex queries using logical operators like AND, OR, NOT, etc. It is used to filter data based on multiple conditions.

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
    # TODO: search and filter functionality
    books = bookData.objects.all()
    return render(request, 'BookTable.html', {'books': books})


def book_add(request):
    if request.method=='POST':
        form=bookDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_table")
    else:
        form = bookDataForm()
    return render(request, 'BookAdd.html', {"form": form})


def book_details(request, book_id):
    book = bookData.objects.get(id=book_id)
    return render(request, 'BookDetails.html', {'book': book})


def book_edit(request, book_id):
    book = bookData.objects.get(id=book_id)
    if request.method == 'POST':
        form=bookDataForm(request.POST, instance=book) # instance means prefilling data of user in form.
        if form.is_valid():
            form.save()
            return redirect("book_table")
    else:
        form=bookDataForm(instance=book)
    return render(request, 'BookEdit.html', {"form": form, "book": book})


def book_delete(request, book_id):
    book = bookData.objects.get(id=book_id)
    book.delete()   # delete from database
    return redirect("book_table")

#i_contains used for case-insensitive search
def user_table(request):
    name_search = request.GET.get("name")
    email_search = request.GET.get("email")
    users = userData.objects.all()
    if name_search or email_search:
        users = users.filter(
            Q(full_name__icontains=name_search) | Q(email__icontains=email_search)
        )
    # with matching fullname or email 
    return render(request, "UserTable.html", {"users": users, "name_search": name_search, "email_search": email_search})


def user_add(request):
    if request.method == 'POST':
        form=userDataForm(request.POST)
        if form.is_valid(): 
            form.save() # saves the data into the database
            return redirect("user_table")
        else: 
            return render(request, 'UserAdd.html', {"form":form})   # idk how {"form":form} works
    return render(request, 'UserAdd.html')


def user_details(request, user_id):
    user=userData.objects.get(id=user_id)
    return render(request, 'UserDetails.html', {"user": user})


def user_edit(request, user_id):
    user=userData.objects.get(id=user_id)
    if request.method == 'POST':
        form=userDataForm(request.POST, instance=user)  # instance means prefilling data of user in form.
        if form.is_valid():
            form.save()
            return redirect("user_table")
    else:
        form=userDataForm(instance=user)
    return render(request, 'UserEdit.html', {"form": form, "user": user})


def user_delete(request, user_id):
    user = userData.objects.get(id=user_id)
    user.delete()   # delete from database
    return redirect("user_table")


def records_open(request):
    records=issueBookData.objects.filter(status='issued')
    return render(request, 'RecordsOpen.html', {"records": records})


def records_closed(request):
    return render(request, 'RecordsClosed.html')


def records_borrow(request):
    user=userData.objects.all()
    book=bookData.objects.all() # filter(available__gt=0) # only show books with available copies > 0
    if request.method == 'POST':
        form = issueBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("records_open")
        else:
            return render(request, 'RecordsBorrowBook.html', {"form":form})
    return render(request, 'RecordsBorrowBook.html',{"users": user, "books": book})
