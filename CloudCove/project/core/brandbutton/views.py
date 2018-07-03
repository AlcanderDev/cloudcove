from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegisterBrandButtonForm
from django import forms
from .models import BrandUser
from django.http import HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.
@login_required()
def home(request):

    if request.user.is_registered == False:
        return HttpResponseRedirect('/connectbutton/')
    return render(request, 'home.html')
    
    
    
def connectbutton(request):
    if request.user.is_registered == True:
        return HttpResponseRedirect('/set-button-ap-mode/')
        
    if request.method == 'POST':
        form = RegisterBrandButtonForm(request.POST)
        if form.is_valid():
            
            request.user.buttonid = form.cleaned_data['buttonid']
            request.user.is_registered = True
            request.user.brand = 'goodlook'
            request.user.networkssid = form.cleaned_data['networkname']
            request.user.networkpwd = form.cleaned_data['networkpassword']
            request.user.save()
            return HttpResponseRedirect('/set-button-ap-mode/')
    else:
        form = RegisterBrandButtonForm()
    return render(request, 'connectbutton.html', {'form': form})
    
def setbuttonapmode(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/connect-with-button/')
    return render(request, 'set-button-ap-mode.html')
    
def connectwithbutton(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            return JsonResponse({'"wifi_ssid" : ' + '"'+ request.user.networkssid + '"' +
                                            ', "wifi_pwd" : ' + '"'+ request.user.networkpassword + '"' +
                                            ', "api_endpoint" : "https://52.221.167.53/button/iot/"' + 
                                            ', "device" : "60C5A86A9CBF'})
            return HttpResponseRedirect('/buttonconnected/')
    return render(request, 'connect-with-button.html')
    
def buttonconnected(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    return render(request, 'buttonconnected.html')