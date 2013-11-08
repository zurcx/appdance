# encoding: utf-8

from django.shortcuts import render

from models import Event


def index(request):
	template_name = 'events/index.html'
	context = {}
	context['events'] = Event.objects.all()
	return render(request, template_name, context)