from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^order/(?P<order_id>[-\w]+)/$', views.order_view, name='order_view'),
    url(r'^reorder/(?P<order_id>[-\w]+)/$', views.order_reorder, name='order_reorder')
]