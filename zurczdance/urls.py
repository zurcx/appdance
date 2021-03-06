from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventos/', include('apps.events.urls')),
    url(r'^galeria/', include('apps.gallery.urls')),
    url(r'^danca/', include('apps.dances.urls')),
    url(r'^', include('apps.core.urls')),
)
