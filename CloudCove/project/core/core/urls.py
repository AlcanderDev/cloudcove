"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as rest_framework_views
from account import views as accounts_views
from brandbutton import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('admin/', admin.site.urls),
    url(r'^registerbutton1/(?P<username>[-\w]+)/(?P<orderid>[-\w]+)/$', views.registerbutton1, name='registerbutton1'),
    url(r'^registerbutton2/(?P<username>[-\w]+)/(?P<orderid>[-\w]+)/$', views.registerbutton2, name='registerbutton2'),
    url(r'^registerbutton3/(?P<username>[-\w]+)/(?P<orderid>[-\w]+)/$', views.registerbutton3, name='registerbutton3'),
    url(r'^registerbutton4/(?P<username>[-\w]+)/(?P<orderid>[-\w]+)/$', views.registerbutton4, name='registerbutton4'),
    url(r'^connectbutton/$', views.connectbutton, name='connectbutton'),
    url(r'^set-button-ap-mode/$', views.setbuttonapmode, name='set-button-ap-mode'),
    url(r'^connect-with-button/$', views.connectwithbutton, name='connect-with-button'),
    url(r'^buttonconnected/$', views.buttonconnected, name='buttonconnected'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html', subject_template_name='password_reset_subject.txt'), name='password_reset'),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'), 
    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
