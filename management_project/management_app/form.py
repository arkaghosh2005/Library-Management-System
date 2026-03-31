from django import forms
from django.core.exceptions import ValidationError 
from .models import *

# cleaned_data is validated&cleaned data using is_valid()
# if errors are found at any time, then they are stored in forms.errors
class userDataForm(forms.ModelForm):
    class Meta:
        model = userData
        fields = ['full_name', 'phone_no', 'email', 'address']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')  
        if not full_name or len(full_name.split()) < 2: # not fullname-> no blank
            raise ValidationError("Please enter Full Name") #catched by form.is_valid() in views.py
        return full_name    
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please enter Email")
        
        unique_email=userData.objects.filter(email=email) # existing user with mail

        if self.instance and self.instance.pk:  # is it a old instance? if yes does it have pk?
            unique_email = unique_email.exclude(pk=self.instance.pk)    # remove this from the checklist

        if unique_email.exists():
            raise forms.ValidationError("Email already exists")
        return email
    

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if (not phone_no) or (not phone_no.isdigit()) or (len(phone_no) != 10) or (phone_no.startswith('0')):
            raise forms.ValidationError("Phone Number must be 10 digits")
        return phone_no
    
    def clean_address(self):
        address = self.cleaned_data.get('address')
        return address
   

class bookDataForm(forms.ModelForm):
    class Meta:
        model = bookData
        # available is set from stock for new books in bookData.save().
        fields = ['book_name', 'author_name', 'book_type', 'stock']

    def clean_book_name(self):
        book_name = self.cleaned_data.get('book_name')  
        if not book_name:
            raise ValidationError("Please enter Book Name") 
        return book_name
    def clean_author_name(self):
        author_name= self.cleaned_data.get('author_name')
        if not author_name:
            raise ValidationError("Please enter Author Name")
        return author_name
    def clean_book_type(self):
        book_type = self.cleaned_data.get('book_type')
        if not book_type:
            raise ValidationError("Please select Book Type")
        return book_type

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None or stock < 0:
            raise ValidationError("Stock must be a non-negative integer")
        return stock
    
    