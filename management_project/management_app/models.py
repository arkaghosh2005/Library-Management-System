from django.db import models
from datetime import timedelta

# (database, frontend)
ISSUE_STATUS = [
    ('issued', 'Issued'),  
    ('returned', 'Returned'),
]

class userData(models.Model):
    full_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    
class bookData(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=150)
    book_type = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)

class issueBookData(models.Model):
    user = models.ForeignKey(userData, on_delete=models.CASCADE)
    book = models.ForeignKey(bookData, on_delete=models.CASCADE)
    author = models.ForeignKey(bookData, on_delete=models.CASCADE, related_name='issued_book')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=None, blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    fine_amount = models.FloatField(default=0.00)
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default='issued')