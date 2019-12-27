from django import forms
from django.contrib.auth.models import User
from .models import Customer, Deliveryguy
from django.contrib.auth.forms import UserCreationForm

DOCTYPE = [
    ('adhaar', 'Adhaar Card'),
    ('electbill', 'Electricity Bill'),
    ('pan', 'PAN Card'),
    ('voting', 'Voting Card')
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['name', 'email', 'password', 'image', 'address_line1', 'address_line2', 'phone', 'zip_code']


class DelvrygyFormCreate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    docname = forms.ChoiceField(
        label='Select the doctype and update its corresponding Photo: ',
        choices=DOCTYPE,
        widget=forms.RadioSelect(),
        required=True)

    class Meta:
        model = Deliveryguy
        fields = [
            'name',
            'email',
            'password',
            'image',
            'address_line1',
            'address_line2',
            'zip_code',
            'drvlicence',
            'docname',
            'verfdoc'
            ]
