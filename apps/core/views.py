# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForm


class HomeView(TemplateView):
	template_name = 'core/home.html'

def contact(request):
	context = {}
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.send_mail()
			context['success'] = True
	else:

		form = ContactForm()
	context['form'] = form
	return render(request, 'core/contact.html', context)

