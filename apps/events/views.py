# encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from django.core.paginator import (Paginator , PageNotAnInteger, EmptyPage)

from models import Event
from forms import CommentForm


def index(request):
	template_name = 'events/index.html'
	context = {}
	events = Event.objects.all()
	search = request.GET.get('search', '')
	if search:
		events = events.filter(Q(name__icontains=search) \
							 | Q(description__icontains=search))

	paginator = Paginator(events, 1)
	page = request.GET.get('page', 1)
	try:
		page_obj = paginator.page(page)
	except PaginatorNotAnInteger:
		page_obj = paginator.page(1)
	except EmptyPage:
		page_obj = paginator.page(page.num_pages)

	context['paginator'] = paginator
	context['page_obj'] = page_obj
	context['events'] = events
	context['search'] = search
	return render(request, template_name, context)

def details(request, pk):
	event = get_object_or_404(Event, pk=pk)
	template_name = 'events/details.html'
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.event = event
			comment.save()
			return redirect('events_details', event.pk)

	else:
		form = CommentForm
	context = {
		'event': event,
		'comment_form': form,
	}
	return render(request, template_name, context)

