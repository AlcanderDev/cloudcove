from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegisterBrandButtonForm
from django import forms
from .models import BrandUser
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import get_object_or_404
from brandbutton.models import BrandUser as btnUser
# Create your views here.
@login_required()
@csrf_exempt
def home(request):
    if request.user.is_registered == False:
        return HttpResponseRedirect('/connectbutton/')
    if request.method =='POST':
        if request.POST.get('btn1') and request.user.button1Order != "":
            return HttpResponseRedirect('http://127.0.0.1:8000/orders/reorder/' + request.user.button1Order + '/')
        if request.POST.get('btn2') and request.user.button2Order != "":
            return HttpResponseRedirect('http://127.0.0.1:8000/orders/reorder/'+ request.user.button2Order + '/')
        if request.POST.get('btn3') and request.user.button3Order != "":
            return HttpResponseRedirect('http://127.0.0.1:8000/orders/reorder/'+ request.user.button3Order + '/')
        if request.POST.get('btn4') and request.user.button4Order != "":
            return HttpResponseRedirect('http://127.0.0.1:8000/orders/reorder/'+ request.user.button4Order + '/')
    return render(request, 'home.html')

@csrf_exempt
def registerbutton1(request, username, orderid):
    if request.method =='GET':
        print('I am here')
        user = get_object_or_404(btnUser, username=username)
        user.button1Order = orderid
        user.save()
        return render(request, 'registerbutton1.html')
    return render(request, 'home.html')
    
def registerbutton2(request, username, orderid):
    if request.method =='GET':
        print('I am here')
        user = get_object_or_404(btnUser, username=username)
        user.button2Order = orderid
        user.save()
        return render(request, 'registerbutton1.html')
    return render(request, 'home.html')
    
def registerbutton3(request, username, orderid):
    if request.method =='GET':
        print('I am here')
        user = get_object_or_404(btnUser, username=username)
        user.button3Order = orderid
        user.save()
        return render(request, 'registerbutton1.html')
    return render(request, 'home.html')

def registerbutton4(request, username, orderid):
    if request.method =='GET':
        print('I am here')
        user = get_object_or_404(btnUser, username=username)
        user.button4Order = orderid
        user.save()
        return render(request, 'registerbutton1.html')
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