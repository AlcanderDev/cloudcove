from django import forms
from django.contrib.auth.models import User
from .models import BrandUser
class RegisterBrandButtonForm(forms.Form):
    buttonid = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    networkname = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    networkpassword = forms.CharField(max_length=254, required=True, widget=forms.PasswordInput())
    class Meta:
        model = BrandUser
        fields = ('buttonid', 'networkname','networkpassword')