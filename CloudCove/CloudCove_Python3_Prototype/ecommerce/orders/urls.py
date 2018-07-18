from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^registerbutton1/(?P<order_id>[-\w]+)/$', views.order_registerButton1, name='order_registerbutton1'),
    url(r'^registerbutton2/(?P<order_id>[-\w]+)/$', views.order_registerButton2, name='order_registerbutton2'),
    url(r'^registerbutton3/(?P<order_id>[-\w]+)/$', views.order_registerButton3, name='order_registerbutton3'),
    url(r'^registerbutton4/(?P<order_id>[-\w]+)/$', views.order_registerButton4, name='order_registerbutton4'),
    url(r'^order/(?P<order_id>[-\w]+)/$', views.order_view, name='order_view'),
    url(r'^reorder/(?P<order_id>[-\w]+)/$', views.order_reorder, name='order_reorder'),
    url(r'^api/(?P<order_id>[-\w]+)/', views.order_button_api, name='order_button_api')
]