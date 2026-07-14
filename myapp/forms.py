from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import Customer

class CustRegFrm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile')

class CustLogFrm(AuthenticationForm):
    username = forms.CharField(
        label=("Username"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary'})
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary'})
    )

class MyChngFrm(UserChangeForm):
    password = None
    username = None
    first_name = forms.CharField(
        label=("First Name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary'})
    )
    last_name = forms.CharField(
        label=("Last Name"),
        widget=forms.TextInput(attrs={'class': 'form-control border-primary'})
    )
    email = forms.CharField(
        label=("Email-ID"),
        widget=forms.EmailInput(attrs={'class': 'form-control border-primary'})
    )
    mobile = forms.CharField(
        label=("Contact Number"),
        widget=forms.NumberInput(attrs={'class': 'form-control border-primary'})
    )
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'mobile')

class PwdChng(PasswordChangeForm):
    old_password = forms.CharField(label=("Current Password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label=("New Password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
