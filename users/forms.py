from django import forms
from django.contrib.auth.models import User
from .models import Customer, Deliveryguy
from django.contrib.auth.forms import UserCreationForm

DOCTYPE = [
    ("adhaar", "Adhaar Card"),
    ("electbill", "Electricity Bill"),
    ("pan", "PAN Card"),
    ("voting", "Voting Card"),
]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomerCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True)
    address_line1 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 20}),
        max_length=255,
        required=True,
    )

    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "password",
            "image",
            "address_line1",
            "address_line2",
            "phone",
            "zip_code",
        ]


class DelvrygyCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, required=True)
    docname = forms.ChoiceField(
        label="Select the doctype and update its corresponding Photo: ",
        choices=DOCTYPE,
        widget=forms.RadioSelect(),
        required=True,
    )

    class Meta:
        model = Deliveryguy
        fields = [
            "name",
            "email",
            "password",
            "image",
            "phone",
            "address_line1",
            "address_line2",
            "zip_code",
            "drvlicence",
            "docname",
            "verfdoc",
        ]
