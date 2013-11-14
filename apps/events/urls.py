# encoding: utf-8

from django.conf.urls import patterns, include, url

from .views import index


urlpatterns = patterns('apps.events.views',

	url(r'^$', "index", name="events"),
	url(r'^(?P<pk>\d+)/$', "details", name="events_details"),

)