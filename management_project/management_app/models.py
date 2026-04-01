from django.db import models
from datetime import date, timedelta

FINE_PER_DAY = 5  # Rs. 5 per day

# (database, frontend)
ISSUE_STATUS = [
    ('issued', 'Issued'),  
    ('returned', 'Returned'),
]
BOOK_TYPE = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science', 'Science'),
    ('History', 'History'),
    ('Biography', 'Biography'),
    ('Technology', 'Technology'),
    ('Literature', 'Literature'),
    ('Other','Other')]


def default_due_date():
    return date.today() + timedelta(days=14)

class userData(models.Model):
    full_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    
class bookData(models.Model):
    book_name = models.CharField(max_length=200, null=False)
    author_name = models.CharField(max_length=150, null=False)
    book_type = models.CharField(max_length=20, choices=BOOK_TYPE, null=False)
    stock = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self._state.adding:
            # New book: available = stock
            self.available = self.stock
        else:
            # Editing existing book: adjust available by the stock difference
            old = bookData.objects.get(pk=self.pk)
            stock_diff = self.stock - old.stock
            self.available = max(self.available + stock_diff, 0)
        super().save(*args, **kwargs)

class issueBookData(models.Model):
    user = models.ForeignKey(userData, on_delete=models.CASCADE)
    book = models.ForeignKey(bookData, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add= True)
    due_date = models.DateField(default=default_due_date)   # 14 days from issue_date
    return_date = models.DateTimeField(blank=True, null=True)
    fine_amount = models.FloatField(default=0.00)
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default='issued')

    @property
    def current_fine(self):
        if self.status == 'issued':
            overdue_days = (date.today() - self.due_date).days
            return max(overdue_days * FINE_PER_DAY, 0)
        return self.fine_amount