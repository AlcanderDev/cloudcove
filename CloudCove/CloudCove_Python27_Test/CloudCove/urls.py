from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'CloudCove.cloudapp.views.index'),
    url(r'^update/', 'CloudCove.cloudapp.views.update'),
    url(r'^delete/', 'CloudCove.cloudapp.views.delete'),
)
