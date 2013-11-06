from django.conf.urls import patterns, include, url
from .views import HomeView, contact

urlpatterns = patterns('',

	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^contato', 'apps.core.views.contact', name='contact'),

)
