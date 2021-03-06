# encoding: utf-8

from django.conf.urls import patterns, include, url 

from .views import TemplateView, RhythmListView, RhythmDetailsView, dancestep_sorted


urlpatterns = patterns('apps.dances.views',

	url(r'^$', TemplateView.as_view(template_name='core/dances.html'), name="dances"),
	url(r'^ritimos/$', RhythmListView.as_view(), name="rhythms"),
	url(r'^ritimos/(?P<pk>\d+)/$', RhythmDetailsView.as_view(), name="rhythms_details"),
	url(r'^ritimos/(?P<pk>\d+)/sorteado/$', 'dancestep_sorted', name="rhythms_sorted"),

)