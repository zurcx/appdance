#encoding: utf-8

from django.conf.urls import patterns, include, url 

from .views import signup

urlpatterns = patterns('core.accounts.views',
	url(r'^cadastro/$', 'signup', name='signup'),
)