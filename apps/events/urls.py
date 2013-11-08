# encoding: utf-8

from django.conf.urls import patterns, include, url

from .views import index


urlpatterns = patterns('',

	url(r'^$', "apps.events.views.index", name="events"),

)