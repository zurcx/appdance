# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
	template_name = 'core/home.html'

def contact(request):
	context = {
		
	}
	return render(request, 'core/contact.html', context)

