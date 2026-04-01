from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q  
from django.utils import timezone
from datetime import timedelta
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
    books = bookData.objects.all().order_by('-id')
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
    users = userData.objects.all().order_by('-id')
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
    # if issueBookData.objects.filter(user=user, status='issued').exists():
    #     # Check if the user has any issued books
    #     return render(request, 'UserDeleteError.html', {"user": user})
    user.delete()   # delete from database
    return redirect("user_table")


def records_open(request):
    search_query = request.GET.get("search", "").strip()
    date_from = request.GET.get("date_from", "").strip()
    date_to = request.GET.get("date_to", "").strip()

    records = issueBookData.objects.filter(status='issued').select_related('user', 'book').order_by('-issue_date', '-id')

    if search_query:
        records = records.filter(
            Q(user__full_name__icontains=search_query)
            | Q(user__email__icontains=search_query)
            | Q(book__book_name__icontains=search_query)
            | Q(book__author_name__icontains=search_query)
        )   # icontains is used for case-insensitive search
    
    if date_from and date_to:
        records = records.filter(
            Q(issue_date__gte=date_from) # gte-> greater than or equal to
            & Q(due_date__lte=date_to)  # lte-> less than or equal to
        )

    return render(
        request,
        'RecordsOpen.html', 
        {
            "records": records,
            "search_query": search_query, 
            "date_from": date_from, 
            "date_to": date_to
        },
    )


def records_closed(request):
    search_query = request.GET.get("search", "").strip()
    date_from = request.GET.get("date_from", "").strip()
    date_to = request.GET.get("date_to", "").strip()

    records = issueBookData.objects.filter(status='returned').select_related('user', 'book').order_by('-return_date', '-id')

    if search_query:
        records = records.filter(
            Q(user__full_name__icontains=search_query)
            | Q(user__email__icontains=search_query)
            | Q(book__book_name__icontains=search_query)
            | Q(book__author_name__icontains=search_query)
        )

    if date_from:
        records = records.filter(return_date__date__gte=date_from)

    if date_to:
        records = records.filter(return_date__date__lte=date_to)

    return render(
        request,
        'RecordsClosed.html',
        {
            "records": records,
            "search_query": search_query,
            "date_from": date_from,
            "date_to": date_to,
        },
    )


def records_borrow(request):
    user = userData.objects.exclude(issuebookdata__status='issued') # __ is used to access related fields in Django ORM.
    book = bookData.objects.filter(available__gt=0) # available__gt=0 means available greater than 0
    if request.method == 'POST':
        form = issueBookForm(request.POST)
        if form.is_valid():
            issue = form.save()
            issue.book.available -= 1
            issue.book.save(update_fields=['available'])
            return redirect("records_open")
        else:
            return render(request, 'RecordsBorrowBook.html', {"form": form, "users": user, "books": book})
    form = issueBookForm()
    return render(request, 'RecordsBorrowBook.html', {"form": form, "users": user, "books": book})


def return_book(request, record_id):
    record = get_object_or_404(issueBookData, id=record_id)
    # get_object_or_404 will raise 404 if id is not found.
    if record.status == 'issued':
        record.status = 'returned'
        record.return_date = timezone.now()
        # Calculate fine if returned after due date
        overdue_days = (record.return_date.date() - record.due_date).days
        if overdue_days > 0:
            record.fine_amount = overdue_days * FINE_PER_DAY
        record.book.available += 1  
        record.book.save(update_fields=['available'])   
        record.save(update_fields=['status', 'return_date', 'fine_amount'])
    # update_fields-> only change these in database
    return redirect('records_open')


def reissue_book(request, record_id):
    record = get_object_or_404(issueBookData, id=record_id)
    if record.status == 'issued':
        today = timezone.now().date()
        record.issue_date = today
        record.due_date = today + timedelta(days=14)
        record.save(update_fields=['issue_date', 'due_date'])
    return redirect('records_open')
