# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)


from django.views.generic import ListView, TemplateView, DetailView

from .models import Rhythm

class RhythmListView(ListView):

	template_name = "dances/index.html"
	paginate_by = 3

	def get_queryset(self):
		rhythms = Rhythm.objects.all()
		search = self.request.GET.get('search', '')
		if search:
			rhythms = rhythms.filter(Q(name__iconstains=search) \
									|Q(description__icontains=search))
		return rhythms

	def get_context_data(self, **kwargs):
		context = super(RhythmListView, self).get_context_data(**kwargs)
		context['search'] = self.request.GET.get('search', '')
		return context


class RhythmDetailsView(DetailView):

	template_name = "dances/rhythm_details.html"

	def get_queryset(self):
		return Rhythm.objects.all()

	def get_context_data(self, **kwargs):
		context = super(RhythmDetailsView, self).get_context_data(**kwargs)
		return context


class DanceStepDetailView(DetailView):

	template_name = "dances/rhythm_step_sorted.html"

	def get_queryset(self):
		return Rhythm.objects.all()

	def get_context_data(self, **kwargs):
		context = super(DanceStepDetailView, self).get_context_data(**kwargs)
		return context


def dancestep_sorted(request, pk):
	rhythm = get_object_or_404(Rhythm, pk=pk)
	template_name = "dances/sortedsteps.html"
	rhythm_slug = rhythm.slug
	n = 4
	rhythm = get_object_or_404(Rhythm, slug=rhythm_slug)
	items = list(rhythm.dancesteps.all().order_by('?')[:n])
	context = {
		'items':items,
		'rhythm':rhythm,
	}

	return render(request, template_name, context)

		






# def details(request, pk):

# 	rhythms = get_object_or_404(Rhythm, pk=pk)
# 	template_name = "dances/details.html"
# 	context = {
# 		'rhythms': rhythms
# 	}

# 	return render (request, template_name, context)


