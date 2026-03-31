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
        if userData.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if (not phone_no) or (not phone_no.isdigit()) or (len(phone_no) < 10) or (phone_no.startswith('0')):
            raise forms.ValidationError("Please enter 10 digit valid Phone Number")
        return phone_no
    
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Please enter Address")
        # TODO: check for city and district?
        return address
   

class bookDataForm(forms.ModelForm):
    class Meta:
        model = bookData
        fields = ['book_name', 'author_name', 'book_type', 'stock', 'available']
