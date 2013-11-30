# encoding: utf-8

from django.conf.urls import patterns, include, url

from .views import EventListView


urlpatterns = patterns('apps.events.views',

	url(r'^$', EventListView.as_view(), name="events"),
	url(r'^(?P<pk>\d+)/$', "details", name="events_details"),

)