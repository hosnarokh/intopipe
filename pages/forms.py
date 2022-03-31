from captcha.fields import CaptchaField
from django import forms
from django.db import transaction
from pages.models import Contact
from customers.models import Order, Customer


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'company',
            'email',
            'phone_number',
            'message',
        ]
        labels = {
            "first_name": 'First Name',
            "last_name": 'Last Name',
            "company": 'Company',
            "email": 'Email',
            "phone_number": 'Phone Number',
            "message": 'Message',
            'captcha': 'Captcha'
        }


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=100, required=True)
    logo = forms.FileField(required=False)
    phone = forms.CharField(max_length=200, required=False) #phone

    class Meta:
        model = Order
        exclude = ("status","customer")


