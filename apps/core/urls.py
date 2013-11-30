from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView, contact

from django.views.generic import TemplateView

urlpatterns = patterns('',

	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^contas/', 'apps.accounts.views.signup', name="signup"),
	#url(r'^galerias/', 'apps.gallery.views.', name="event_gallery"),  #verificar necessidade
	url(r'^entrar/$', 'django.contrib.auth.views.login',
		{'template_name': 'core/login.html'}, name='login'),
	url(r'^sair/$', 'django.contrib.auth.views.logout',
		{'next_page': '/'}, name='logout'),
	url(r'^contato', 'apps.core.views.contact', name='contact'),
	url(r'^lista-recursos/', TemplateView.as_view(template_name="core/listarecursos.html"), name='listarecursos')
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
	urlpatterns += patterns(''
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
	)