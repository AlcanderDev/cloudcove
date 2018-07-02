from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from brandbutton.models import BrandUser
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    address = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    class Meta:
        model = BrandUser
        fields = ('username', 'email', 'address', 'password1', 'password2')