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
    website = forms.URLField(max_length=200, required=False) #phone

    class Meta: 
        model = Order 
        exclude = ("status","customer")
 
    @transaction.atomic 
    def save(self, commit=True): 
        name = self.cleaned_data.get("name") 
        email = self.cleaned_data.get("email") 
        logo = self.cleaned_data.get("logo") 
        website = self.cleaned_data.get("website") 
        customer = customer.objects.create(name=name, logo = logo,
        website=website, email= email) 
        customer.save()

        material= self.cleaned_data.get("material") 
        inner_diameter = self.cleaned_data.get("inner_diameter") 
        thickness = self.cleaned_data.get("thickness") 
        length = self.cleaned_data.get("length")
        quantity = self.cleaned_data.get("quantity") 
        
        order = Order.objects.create(customer=customer, material = material, 
        inner_diameter = inner_diameter, thickness = thickness, length = length, 
        quantity=quantity)
        order.save()

        return customer, order
 
 




    def __init__(self, *args, **kwargs): 
        super(OrderForm, self).__init__(*args, **kwargs) 
 
        self.fields['username'].widget.attrs['class'] = 'form-control' 
        self.fields['password'].widget.attrs['class'] = 'form-control' 
        self.fields['password2'].widget.attrs['class'] = 'form-control' 
        self.fields['first_name'].widget.attrs['class'] = 'form-control' 
        self.fields['last_name'].widget.attrs['class'] = 'form-control' 
        self.fields['email'].widget.attrs['class'] = 'form-control' 
        self.fields['name'].widget.attrs['class'] = 'form-control' 
        self.fields['is_main'].widget.attrs['class'] = 'form-control' 
        self.fields['description'].widget.attrs['class'] = 'form-control' 
        self.fields['food_restaurant_category'].widget.attrs['class'] = 'form-control' 
        self.fields['restaurant'].widget.attrs['class'] = 'form-control' 
        self.fields['city'].widget.attrs['class'] = 'form-control' 
        self.fields['address'].widget.attrs['class'] = 'form-control' 
