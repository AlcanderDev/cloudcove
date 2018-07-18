from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    first_name =  forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    last_name =  forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    address =  forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    postal_code =  forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    city =  forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'address', 'postal_code', 'city')